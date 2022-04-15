from Variables_Fixes import *

#Root window
root = tk.Tk()
w = root.winfo_height
root.geometry("550x200")
root.title("Valeur actuelle nette")
root.configure(bg = 'white')

#labels
label = Label(root,text = "La valeur actuelle nette est", font = 'arial', bg = 'white')
label.grid(row = 7,column = 0, sticky = 'e')
label_kwh = Label(root , text = "Prix du KWh est (en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')
label_taux = Label(root , text = "Le taux de croissance économique est : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
label_inv = Label(root , text = "L'investissement est : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w')
label_capacite= Label(root,text= "La capacité installé:", font='arial', bg = 'white'). grid(row = 5, column = 0, sticky = 'w')
valeur = Label(root,text = "0.0$", font = 'arial', fg = 'red', bg = 'white')
valeur.grid(row = 7,column = 2, sticky = 'w')


#Fonctions
def Button(event):
   kwh.set(str(Prix_Du_KWh[drop.get()]))
   taux.set(taux_croiss_eco)
   inv.set(str(Investissement[drop.get()]))


def calcul_de_prix():
   if(drop.get() == ''):
      messagebox.showerror(title = "Error", message = "Please select an energy source!")
   else:
      if(kwh.get() == ''):
         kwh.set(str(Prix_Du_KWh[drop.get()]))
      if(taux.get() == ''):
         taux.set(str(taux_croiss_eco))
      if(inv.get() == ''):
         inv.set(str(Investissement[drop.get()]))
      if(capacite.get() == ''):
         messagebox.showerror(title = "Error", message = "Please enter a capacity!")
      try:
         production=float(capacite.get())*24*365*Coef_De_Charge[drop.get()]
         gain=production*(Prix_Du_KWh["Fuel-based"] - float(kwh.get()))
         facteur=(1-(1/(1+float(taux.get()))**31))/float(taux.get())
         van=gain*facteur-float(inv.get())
         valeur['text'] = str("%.3f" %van)
      except ZeroDivisionError:
         messagebox.showerror('Division par 0', message =  "La taux de croissance économique ne peut pas etre nul!")

def reset():
   drop.set('')
   kwh.set('')
   taux.set('')
   inv.set('')
   capacite.set('')


#ComboBox
select = Label(root,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 1, column = 0,sticky='w')
drop = ttk.Combobox(root, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
drop.grid(row = 1, column = 2, columnspan = 2)
drop.bind('<<ComboboxSelected>>', Button)

#variable
inv = StringVar()
kwh = StringVar()
taux = StringVar()
capacite = StringVar()

#Input labels
kwh_input = tk.Entry(root, width = 30, textvariable = kwh).grid(row = 2, column = 2, columnspan = 2)
taux_input = tk.Entry(root, width = 30, textvariable = taux).grid(row = 3, column = 2, columnspan = 2)
inv_input = tk.Entry(root, width = 30, textvariable = inv).grid(row = 4, column = 2, columnspan = 2)
capacite_entry=tk.Entry(root, width = 30, textvariable = capacite).grid(row = 5, column = 2, columnspan = 2)

#buttons
button = ttk.Button( root , text = "Calcul", command = calcul_de_prix ).grid(row = 6, column = 3)
reset_btn = ttk.Button(root, text = "Reset", command = reset).grid(row = 6, column = 2)


root.mainloop()
