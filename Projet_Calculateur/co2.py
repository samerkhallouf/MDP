from Variables_Fixes import *


class Co2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x200")
        self.title("Prix du KWh")
        self.configure(bg = 'white')
        
        #Labels:
        self.label = Label(self,text = "Emission(Tonnes/MWh produit): ", font = 'arial', bg = 'white')
        self.label.grid(row = 1,column = 0, sticky = 'w')
        self.label_energie = Label(self , text = "Energie(MWh produit): ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')
        self.emission_total = Label(self,text = "0.0 g", font = 'arial', fg = 'red', bg = 'white')
        self.emission_total.grid(row = 6,column = 2, sticky = 'w')
        self.label_emission = Label(self,text = "Le taux d'emission en CO2 est de ", font = 'arial', bg = 'white').grid(row = 6, column = 0)

        #variable
        self.energie = StringVar()
        self.emission = StringVar()
        self.emission_CO2 = StringVar()

        #ComboBox
        self.select = Label(self,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 0, column = 0)
        self.drop = ttk.Combobox(self, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        self.drop.grid(row = 0, column = 2, columnspan = 2)
        self.drop.bind('<<ComboboxSelected>>', self.Button)

        #Input labels:
        self.emissiom_input = tk.Entry(self, width = 30, textvariable = self.emission).grid(row = 1, column = 2, columnspan = 2)
        self.energie_input = tk.Entry(self, width = 30, textvariable = self.energie).grid(row = 2, column = 2, columnspan = 2)

        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul_de_prix ).grid(row = 5, column = 3)
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 5, column = 2)
        self.plot_btn = ttk.Button(self,text = "Graphe", command = self.graphe).grid(row = 5, column = 0)
        self.plot_total_btn = ttk.Button(self,text = "Emission totale", command = Comparaison_CO2).grid(row = 5, column = 1)
    #Fonctions
    def Button(self,event):
        self.emission.set(str(Emission_CO2[self.drop.get()]))

    def calcul_de_prix(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Error", message = "Please select an energy source!")
        else:
            if(self.emission.get() == ''):
                self.emission.set(str(Emission_CO2[self.drop.get()]))
            if( self.energie.get() == ''):
                messagebox.showerror("Incomplet", message = "Veuilez inserer l'energie!")
            else:
                self.emission_CO2.set(str(float(self.emission.get())*float(self.energie.get())))
                self.emission_total["text"] =  "%.3f"%float(self.emission_CO2.get())+ " Tonne(s)"

    def reset(self):
        self.drop.set('')
        self.emission.set('')
        self.energie.set('')

    def graphe(self):
        if (self.emission_CO2.get() == ''):
            messagebox.showerror("Erreur", message="Veuillez remplir l'interface!")

        else:
            plot_window = tk.Tk()
            plot_window.title("Emission de CO2")
            co2 = float("%.3f" % float(self.emission_CO2.get()))
            data = {
                'Heavy-Fuel':Emission_CO2["Heavy-Fuel"]*float(self.energie.get()),
                "Diesel oil":Emission_CO2["Diesel oil"]*float(self.energie.get()),
                "Natural Gas" : Emission_CO2["Natural Gas"]*float(self.energie.get()),
                self.drop.get(): co2
            }
            self.energies = self.data.keys()
            self.emission = self.data.values()
            self.energies= []
            self.emissions = []
            for i in Emission_CO2.keys():
                if(i != self.drop.get()):
                    self.energies.append(i)
                    self.emissions.append(Emission_CO2[i] * float(self.energie.get()))

            self.energies.append(self.drop.get())
            self.emissions.append(co2)
            # create a figure
            figure = Figure(figsize=(6, 4), dpi=100)
            # create FigureCanvasTkAgg object
            figure_canvas = FigureCanvasTkAgg(figure, plot_window)
            # create the toolbar
            NavigationToolbar2Tk(figure_canvas,plot_window)
            # create axes
            axes = self.figure.add_subplot()
            # create the barchart
            axes.bar(self.energies, self.emissions)
            axes.set_title('Emission de CO2')
            axes.set_ylabel('Emission(Tonnes)')

            figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



