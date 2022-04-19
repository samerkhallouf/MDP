from Variables_Fixes import *
from PIL import Image, ImageTk 


class Co2(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        self.title("Emission de CO2")
        self.configure(bg = 'white')
        
        self.bg = Image.open("bg.png")
        self.bg = ImageTk.PhotoImage(self.bg.resize((800,550), Image.ANTIALIAS))
        self.la = Label(self, image = self.bg)
        self.la.place(x = 0, y = 0)

        #Labels:
        self.label = Label(self,text = "Emission (Tonnes/MWh produit): ", font = 'arial', bg = 'white')
        self.label.grid(row = 1,column = 0, sticky = 'w',padx=30,pady=(0,20))
        self.label_energie = Label(self , text = "Energie (MWh produit): ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w',padx=30,pady=(0,20))
        self.emission_total = Label(self,text = "0.0 g", font = 'arial', fg = 'red', bg = 'white')
        self.emission_total.grid(row = 6,column = 2, sticky = 'w')
        self.label_emission = Label(self,text = "Le taux d'emission en CO2 est de ", font = 'arial', bg = 'white').grid(row = 6, column = 0, sticky = 'e',columnspan=2)

        #variable
        self.energie = StringVar()
        self.emission = StringVar()
        self.emission_CO2 = StringVar()

        #ComboBox
        self.select = Label(self,text = "Choisissez votre source d'énergie: ", font = 'arial', bg = 'white').grid(row = 0, column = 0,padx=30,pady=(30,15))
        self.drop = ttk.Combobox(self, width = 47, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        self.drop.grid(row = 0, column = 2, columnspan = 2)
        self.drop.bind('<<ComboboxSelected>>', self.Button)

        #Input labels:
        self.emissiom_input = tk.Entry(self, width = 50, textvariable = self.emission)
        self.emissiom_input.grid(row = 1, column = 2, columnspan = 2)
        self.energie_input = tk.Entry(self, width = 50, textvariable = self.energie)
        self.energie_input.grid(row = 2, column = 2, columnspan = 2)

        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul_de_prix ).grid(row = 5, column = 3,pady=(15,10))
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 5, column = 2,pady=(15,10))
        self.plot_btn = ttk.Button(self,text = "Graphe", command = self.graphe,width=50).grid(row = 7, column = 0,pady=(10,20),columnspan=2)
        self.plot_total_btn = ttk.Button(self,text = "Emission totale", command = Comparaison_CO2,width=50).grid(row = 7, column = 2,columnspan=2,pady=(10,20))
    #Fonctions
    def Button(self,event):
        self.emissiom_input.delete('0',END)
        self.emissiom_input.insert('0',str(Emission_CO2[self.drop.get()]))



    def calcul_de_prix(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Erreur", message = "Choisissez une source d'énergie!")
        else:
            self.emission.set(self.emissiom_input.get())
            self.energie.set(self.energie_input.get())
            if(self.emission.get() == ''):
                self.emission.set(str(Emission_CO2[self.drop.get()]))
            if( self.energie.get() == ''):
                messagebox.showerror("Incomplet", message = "Veuilez insérer l'energie!")
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
            axes = figure.add_subplot()
            # create the barchart
            axes.bar(self.energies, self.emissions)
            axes.set_title('Emission de CO2')
            axes.set_ylabel('Emission (Tonnes)')

            figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



