from Variables_Fixes import *


#Root window
root = tk.Tk()
w = root.winfo_height
root.geometry("450x175")
root.title("Temps De Retour")
root.configure(bg = 'white')

#labels
label_KW = Label(root,text = "Le prix du KWh est:", font = 'arial', bg = 'white')
label_KW.grid(row = 1,column = 0, sticky = 'w')
label = Label(root,text = "Le temps de retour est", font = 'arial', bg = 'white')
label.grid(row = 7,column = 0, sticky = 'e')
label_inv = Label(root , text = "Investissement total (en $) : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
label_KW_installed = Label(root , text = "La capacité est : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')

prix = Label(root,text = "0.0 année", font = 'arial', fg = 'red', bg = 'white')
prix.grid(row = 7,column = 2, sticky = 'w')


#Fonctions
def Button(event):
   prix_kwh.set(str(Prix_Du_KWh[drop.get()]))
   kw_installed.set(str(Capacite[drop.get()]))


def calcul():
   if(drop.get() == ''):
      messagebox.showerror(title = "Error", message = "Please select an energy source!")
   else:
      if(prix_kwh.get() == ''):
         prix_kwh.set(str(Prix_du_kw[drop.get()]))
      if(kw_installed.get() == ''):
         kw_installed.set(str(Capacite[drop.get()]))
      if(inv.get() == ''):
         messagebox.showerror('Erreur!', message= "Veuillez inserer l'invesstissement ")
      production = float(kw_installed.get())*8760*Coef_De_Charge[drop.get()]
      gain = production *(Prix_Du_KWh["Fuel-based"] - float(prix_kwh.get()))
      TR.set(str(float((inv.get()))/gain))
      prix['text'] = "%.3f année(s)."%float(TR.get())


def reset():
   drop.set('')
   inv.set('')
   prix_kwh.set('')
   kw_installed.set('')

def graphe():
   if(TR.get() == ''):
      messagebox.showerror("Erreur", message="Veuillez remplir l'interface!")

   else:
      plot_window = tk.Tk()
      plot_window.title("Prix du KWh actualisé")
      tr = float("%.3f" % float(TR.get()))
      data = {
         'Fuel-based': Temps_de_retour["Fuel-based"],
         drop.get(): tr
      }
      energies = data.keys()
      cout = data.values()
      # create a figure
      figure = Figure(figsize=(6, 4), dpi=100)
      # create FigureCanvasTkAgg object
      figure_canvas = FigureCanvasTkAgg(figure, plot_window)
      # create the toolbar
      NavigationToolbar2Tk(figure_canvas, plot_window)
      # create axes
      axes = figure.add_subplot()
      # create the barchart
      axes.bar(energies, cout, color = ["red", "green"])

      axes.set_title('Temps de retour')
      axes.set_ylabel('Année(s)')
      figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


#ComboBox
select = Label(root,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 0, column = 0)
drop = ttk.Combobox(root, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
drop.grid(row = 0, column = 2, columnspan = 2)
drop.bind('<<ComboboxSelected>>', Button)

#variable
inv = StringVar()
prix_kwh = StringVar()
kw_installed = StringVar()
TR = StringVar()


#Input labels
inv_input = tk.Entry(root, width = 30, textvariable = inv).grid(row = 3, column = 2, columnspan = 2)
kw_input = tk.Entry(root, width = 30, textvariable = prix_kwh).grid(row = 1, column = 2, columnspan = 2)
kw_installed_input = tk.Entry(root, width = 30, textvariable = kw_installed).grid(row = 2, column = 2, columnspan = 2)

#buttons
button = ttk.Button( root , text = "Calcul", command = calcul ).grid(row = 6, column = 3)
reset_btn = ttk.Button(root, text = "Reset", command = reset).grid(row = 6, column = 2)
plot_btn = ttk.Button(root,text = "Graphe", command = graphe).grid(row = 6, column = 0, sticky = 'w')
plot_btn_total = ttk.Button(root,text = "Comparaison ", command = Comparaison_TR).grid(row = 6, column = 1, sticky = 'w')

root.mainloop()