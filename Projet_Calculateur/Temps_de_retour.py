from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Varables_Fixes import *
#Root window
root = tk.Tk()
w = root.winfo_height
root.geometry("450x175")
root.title("Prix du KWh")
root.configure(bg = 'white')

#labels
label_KW = Label(root,text = "Le prix du KWh est:", font = 'arial', bg = 'white')
label_KW.grid(row = 1,column = 0, sticky = 'w')
label = Label(root,text = "Le temps de retour est", font = 'arial', bg = 'white')
label.grid(row = 7,column = 0, sticky = 'e')
label_inv = Label(root , text = "Investissement total (en $) : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
label_gain = Label(root , text = "Le gain annuel est : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w')
# label_KW_installed = Label(root , text = "Le nombre de KW installé est : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')

prix = Label(root,text = "0.0$", font = 'arial', fg = 'red', bg = 'white')
prix.grid(row = 7,column = 2, sticky = 'w')


#Fonctions
def Button(event):
   inv.set()
   gain.set()

def calcul_de_prix():
   if(drop.get() == ''):
      messagebox.showerror(title = "Error", message = "Please select an energy source!")
   else:
      if(prix_kwh.get() == ''):
         prix_kwh.set(str(Prix_du_kw[drop.get()]))
      if(gain.get() == ''):
         messagebox.showerror('Division par 0', message="Le gain ne peut pas etre nul!")
      if(inv.get() == ''):
         messagebox.showerror('Erreur!', message= "Veuillez inserer l'invesstissement ")
         # inv.set(str(float(prix_kwh.get())*float(kwh_installed.get())))
      try:
         prix['text'] = str(round(float(inv.get())/float(gain.get()))) + "$"
      except ZeroDivisionError:
         messagebox.showerror('Division par 0', message =  "Le gain ne peut pas etre nul!")

def reset():
   drop.set('')
   gain.set('')
   inv.set('')
   prix_kwh.set('')
   # kwh_installed.set('')



#ComboBox
select = Label(root,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 0, column = 0)
drop = ttk.Combobox(root, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
drop.grid(row = 0, column = 2, columnspan = 2)
drop.bind('<<ComboboxSelected>>', Button)

#variable
inv = StringVar()
gain = StringVar()
prix_kwh = StringVar()
kwh_installed = StringVar()


#Input labels
inv_input = tk.Entry(root, width = 30, textvariable = inv).grid(row = 3, column = 2, columnspan = 2)
gain_input = tk.Entry(root, width = 30, textvariable = gain).grid(row = 4, column = 2, columnspan = 2)
kw_input = tk.Entry(root, width = 30, textvariable = prix_kwh).grid(row = 1, column = 2, columnspan = 2)
kw_installed_input = tk.Entry(root, width = 30, textvariable = kwh_installed).grid(row = 2, column = 2, columnspan = 2)

#buttons
button = ttk.Button( root , text = "Calcul" ).grid(row = 6, column = 3)
reset_btn = ttk.Button(root, text = "Reset", command = reset).grid(row = 6, column = 2)


root.mainloop()