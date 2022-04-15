from Variables_Fixes import *


#Root window
root = tk.Tk()
w = root.winfo_height
root.geometry("550x200")
root.title("Prix du KWh")
root.configure(bg = 'white')
frame = Frame(root).grid(row = 0, column = 0)


#labels
label = Label(frame,text = "Le prix du KWh est", font = 'arial', bg = 'white')
label.grid(row = 7,column = 0, sticky = 'e')
label_kw = Label(frame , text = "Prix du KW est(en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w', columnspan = 2)
label_coef = Label(frame , text = "Coefficient de charge est : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w', columnspan = 2)
label_duree = Label(frame , text = "La duree de vie est : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w', columnspan = 2)
label_taux = Label(frame , text = "Le taux de croissance économique est : ", font = 'arial', bg = 'white'). grid(row = 5, column = 0, sticky = 'w', columnspan = 2)
prix = Label(frame,text = "0.0 cents", font = 'arial', fg = 'red', bg = 'white')
prix.grid(row = 7,column = 2, sticky = 'w')


#Fonctions
def Button(event):
   kw.set(str(Prix_du_kw[drop.get()]))
   coef.set(str(Coef_De_Charge[drop.get()]))
   duree.set(str(Duree_De_Vie[drop.get()]))
   taux.set(str(taux_croiss_eco))

def calcul_de_prix():
   if(drop.get() == ''):
      messagebox.showerror(title = "Error", message = "Please select an energy source!")
   else:
      if(kw.get() == ''):
         kw.set(str(Prix_du_kw[drop.get()]))
      if(coef.get() == ''):
         coef.set(str(Coef_De_Charge[drop.get()]))
      if(duree.get() == ''):
         duree.set(str(Duree_De_Vie[drop.get()]))
      if(taux.get() == ''):
         taux.set(str(taux_croiss_eco))
      try:
         prix_kw=(float(kw.get())/(365*24*float(coef.get())*float(duree.get())))
         facteur=(1-(1/(1+float(taux.get()))**31))/float(taux.get())
         prix_du_kwh.set(str(prix_kw * facteur * 100))
         prix['text'] = "%.3f cents" %float(prix_du_kwh.get())
      except ZeroDivisionError:
         messagebox.showerror('Division par 0', message =  "La durée de vie ne peut pas etre nulle!")

def reset():
   drop.set('')
   kw.set('')
   coef.set('')
   duree.set('')
   taux.set('')

def graphe():
   if(prix_du_kwh.get() == ''):
      messagebox.showerror("Erreur", message="Veuillez remplir l'interface!")

   else:
      plot_window = tk.Tk()
      plot_window.title("Prix du KWh actualisé")
      prix_act = float("%.3f" % float(prix_du_kwh.get()))
      data = {
         'Fuel-based': Prix_Du_KWh["Fuel-based"],

         drop.get(): prix_act
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
      axes.bar(energies, cout)
      axes.set_title('Prix du KWh actualisé')
      axes.set_ylabel('Cout')

      figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)




#ComboBox
select = Label(frame,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 1, column = 0, sticky = 'w')
drop = ttk.Combobox(frame, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
drop.grid(row = 1, column = 2, columnspan = 2)
drop.bind('<<ComboboxSelected>>', Button)

#variable
duree = StringVar()
kw = StringVar()
coef = StringVar()
taux = StringVar()
prix_du_kwh = StringVar()


#Input labels
kw_input = Entry(frame, width = 30, textvariable = kw).grid(row = 2, column = 2, columnspan = 2)
coef_input = Entry(frame, width = 30, textvariable = coef).grid(row = 3, column = 2, columnspan = 2)
duree_input = Entry(frame, width = 30, textvariable = duree).grid(row = 4, column = 2, columnspan = 2)
taux_input = Entry(frame, width = 30, textvariable = taux).grid(row = 5, column = 2, columnspan = 2)

#buttons
button = ttk.Button( frame, text = "Calcul", command = calcul_de_prix ).grid(row = 6, column = 3)
reset_btn = ttk.Button(frame, text = "Reset", command = reset).grid(row = 6, column = 2)
plot_btn = ttk.Button(frame,text = "Graphe", command = graphe).grid(row = 6, column = 0, sticky = 'w')
plot_btn_total = ttk.Button(frame,text = "Comparaison ", command = Comparaison_kwh).grid(row = 6, column = 1, sticky = 'w')

root.mainloop()
