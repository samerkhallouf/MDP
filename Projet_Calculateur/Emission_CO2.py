from Variables_Fixes import *


#Root window:
root = tk.Tk()
w = root.winfo_height
root.geometry("600x200")
root.title("Prix du KWh")
root.configure(bg = 'white')

#Labels:
label = Label(root,text = "Emission(Tonnes/MWh produit): ", font = 'arial', bg = 'white')
label.grid(row = 1,column = 0, sticky = 'w')
label_energie = Label(root , text = "Energie(MWh produit): ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')
emission_total = Label(root,text = "0.0 g", font = 'arial', fg = 'red', bg = 'white')
emission_total.grid(row = 6,column = 2, sticky = 'w')
label_emission = Label(root,text = "Le taux d'emission en CO2 est de ", font = 'arial', bg = 'white').grid(row = 6, column = 0)

#variable
energie = StringVar()
emission = StringVar()
emission_CO2 = StringVar()

#Fonctions
def Button(event):
   emission.set(str(Emission_CO2[drop.get()]))

def calcul_de_prix():
   if(drop.get() == ''):
      messagebox.showerror(title = "Error", message = "Please select an energy source!")
   else:
      if(emission.get() == ''):
          emission.set(str(Emission_CO2[drop.get()]))
      if( energie.get() == ''):
          messagebox.showerror("Incomplet", message = "Veuilez inserer l'energie!")
      else:
        emission_CO2.set(str(float(emission.get())*float(energie.get())))
        emission_total["text"] =  "%.3f"%float(emission_CO2.get())+ " Tonne(s)"

def reset():
   drop.set('')
   emission.set('')
   energie.set('')

def graphe():
    if (emission_CO2.get() == ''):
        messagebox.showerror("Erreur", message="Veuillez remplir l'interface!")

    else:
        plot_window = tk.Tk()
        plot_window.title("Emission de CO2")
        co2 = float("%.3f" % float(emission_CO2.get()))
        data = {
            'Heavy-Fuel':Emission_CO2["Heavy-Fuel"]*float(energie.get()),
            "Diesel oil":Emission_CO2["Diesel oil"]*float(energie.get()),
            "Natural Gas" : Emission_CO2["Natural Gas"]*float(energie.get()),
            drop.get(): co2
        }
        energies = data.keys()
        emission = data.values()
        energies= []
        emissions = []
        for i in Emission_CO2.keys():
            if(i != drop.get()):
                energies.append(i)
                emissions.append(Emission_CO2[i] * float(energie.get()))

        energies.append(drop.get())
        emissions.append(co2)
        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)
        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, plot_window)
        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, plot_window)
        # create axes
        axes = figure.add_subplot()
        # create the barchart
        axes.bar(energies, emissions)
        axes.set_title('Emission de CO2')
        axes.set_ylabel('Emission(Tonnes)')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#ComboBox
select = Label(root,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 0, column = 0)
drop = ttk.Combobox(root, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
drop.grid(row = 0, column = 2, columnspan = 2)
drop.bind('<<ComboboxSelected>>', Button)

#Input labels:
emissiom_input = tk.Entry(root, width = 30, textvariable = emission).grid(row = 1, column = 2, columnspan = 2)
energie_input = tk.Entry(root, width = 30, textvariable = energie).grid(row = 2, column = 2, columnspan = 2)

#buttons
button = ttk.Button( root , text = "Calcul", command = calcul_de_prix ).grid(row = 5, column = 3)
reset_btn = ttk.Button(root, text = "Reset", command = reset).grid(row = 5, column = 2)
plot_btn = ttk.Button(root,text = "Graphe", command = graphe).grid(row = 5, column = 0)
plot_total_btn = ttk.Button(root,text = "Emission totale", command = Comparaison_CO2).grid(row = 5, column = 1)

root.mainloop()