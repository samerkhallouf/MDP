from Variables_Fixes import *


class Tdr(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("450x175")
        self.title("Temps De Retour")
        self.configure(bg = 'white')
     

        #labels
        self.label_KW = Label(self,text = "Le prix du KWh est:", font = 'arial', bg = 'white')
        self.label_KW.grid(row = 1,column = 0, sticky = 'w')
        self.label = Label(self,text = "Le temps de retour est", font = 'arial', bg = 'white')
        self.label.grid(row = 7,column = 0, sticky = 'e')
        self.label_inv = Label(self , text = "Investissement total (en $) : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
        self.label_KW_installed = Label(self , text = "La capacité est : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')

        self.prix = Label(self,text = "0.0 année", font = 'arial', fg = 'red', bg = 'white')
        self.prix.grid(row = 7,column = 2, sticky = 'w')

        #ComboBox
        self.select = Label(self,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 0, column = 0)
        self.drop = ttk.Combobox(self, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        self.drop.grid(row = 0, column = 2, columnspan = 2)
        self.drop.bind('<<ComboboxSelected>>', self.Button)

        #variable
        self.inv = StringVar()
        self.prix_kwh = StringVar()
        self.kw_installed = StringVar()
        self.TR = StringVar()


        #Input labels
        self.inv_input = tk.Entry(self, width = 30, textvariable = self.inv).grid(row = 3, column = 2, columnspan = 2)
        self.kw_input = tk.Entry(self, width = 30, textvariable = self.prix_kwh).grid(row = 1, column = 2, columnspan = 2)
        self.kw_installed_input = tk.Entry(self, width = 30, textvariable = self.kw_installed).grid(row = 2, column = 2, columnspan = 2)

        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul ).grid(row = 6, column = 3)
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 6, column = 2)
        self.plot_btn = ttk.Button(self,text = "Graphe", command = self.graphe).grid(row = 6, column = 0, sticky = 'w')
        self.plot_btn_total = ttk.Button(self,text = "Comparaison ", command = Comparaison_TR).grid(row = 6, column = 1, sticky = 'w')

    #Fonctions
    def Button(self,event):
        self.prix_kwh.set(str(Prix_Du_KWh[self.drop.get()]))
        self.kw_installed.set(str(Capacite[self.drop.get()]))


    def calcul(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Error", message = "Please select an energy source!")
        else:
            if(self.prix_kwh.get() == ''):
                self.prix_kwh.set(str(Prix_du_kw[self.drop.get()]))
            if(self.kw_installed.get() == ''):
                self.kw_installed.set(str(Capacite[self.drop.get()]))
            if(self.inv.get() == ''):
                messagebox.showerror('Erreur!', message= "Veuillez inserer l'invesstissement ")
            production = float(self.kw_installed.get())*8760*Coef_De_Charge[self.drop.get()]
            gain = production *(Prix_Du_KWh["Fuel-based"] - float(self.prix_kwh.get()))
            self.TR.set(str(float((self.inv.get()))/gain))
            self.prix['text'] = "%.3f année(s)."%float(self.TR.get())


    def reset(self):
        self.drop.set('')
        self.inv.set('')
        self.prix_kwh.set('')
        self.kw_installed.set('')

    def graphe(self):
        if(self.TR.get() == ''):
            messagebox.showerror("Erreur", message="Veuillez remplir l'interface!")

        else:
            plot_window = tk.Tk()
            plot_window.title("Prix du KWh actualisé")
            tr = float("%.3f" % float(self.TR.get()))
            data = {
                'Fuel-based': Temps_de_retour["Fuel-based"],
                self.drop.get(): tr
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




