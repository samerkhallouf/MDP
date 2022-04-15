from Variables_Fixes import *



#Root window
root = tk.Tk()
w = Frame(root, bg = "white")
w.grid(row = 0, column = 0)
#root.geometry("450x150")
root.title("Prix du KWh")
root.configure(bg = 'white')

#labels
label = Label(w,text = "Le prix du KWh est", font = 'arial', bg = 'white')
label.grid(row = 6,column = 0, sticky = 'e')
label_kw = Label(w , text = "Prix du KW est(en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')
label_coef = Label(w , text = "Coefficient de charge est : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
label_duree = Label(w , text = "La duree de vie est : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w')
prix = Label(w,text = "0.0 cents", font = 'arial', fg = 'red', bg = 'white')
prix.grid(row = 6,column = 2, sticky = 'w')


#Fonctions
def Button(event):
   kw.set(str(Prix_du_kw[drop.get()]))
   coef.set(str(Coef_De_Charge[drop.get()]))
   duree.set(str(Duree_De_Vie[drop.get()]))

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
      try:
         prix_du_kwh.set(str(float(kw.get()) * 100 / (365 * 24 * float(coef.get()) * float(duree.get()))))
         prix['text'] = "%.3f cents"%float(prix_du_kwh.get())
      except ZeroDivisionError:
         messagebox.showerror('Division par 0', message =  "La durée de vie ne peut pas etre nulle!")

def reset():
   drop.set('')
   kw.set('')
   coef.set('')
   duree.set('')

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
select = Label(w,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 1, column = 0)
drop = ttk.Combobox(w, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
drop.grid(row = 1, column = 2, columnspan = 2)
drop.bind('<<ComboboxSelected>>', Button)

#variable
duree = StringVar()
kw = StringVar()
coef = StringVar()
prix_du_kwh = StringVar()


#Input labels
kw_input = tk.Entry(w, width = 30, textvariable = kw).grid(row = 2, column = 2, columnspan = 2)
coef_input = tk.Entry(w, width = 30, textvariable = coef).grid(row = 3, column = 2, columnspan = 2)
duree_input = tk.Entry(w, width = 30, textvariable = duree).grid(row = 4, column = 2, columnspan = 2)

#buttons
button = ttk.Button( w , text = "Calcul", command = calcul_de_prix ).grid(row = 5, column = 3)
reset_btn = ttk.Button(w, text = "Reset", command = reset).grid(row = 5, column = 2)
plot_btn = ttk.Button(w,text = "Graphe", command = graphe).grid(row = 5, column = 0)
plot_btn_total = ttk.Button(w,text = "Comparaison total", command = Comparaison_kwh).grid(row = 5, column =1)

root.mainloop()
