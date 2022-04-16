from Variables_Fixes import *

class Kwh(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Prix du KWh")
        self.configure(bg = 'white')
        self.protocol("WM_DELETE_WINDOW", self.quit_me)

        #labels
        label = Label(self,text = "Le prix du KWh est", font = 'arial', bg = 'white')
        label.grid(row = 6,column = 0, sticky = 'e')
        self.label_kw = Label(self , text = "Prix du KW est(en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')
        self.label_coef = Label(self , text = "Coefficient de charge est : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
        self.label_duree = Label(self , text = "La duree de vie est : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w')
        prix = Label(self,text = "0.0 cents", font = 'arial', fg = 'red', bg = 'white')
        prix.grid(row = 6,column = 2, sticky = 'w')

         #ComboBox
        self.select = Label(self,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 1, column = 0)
        drop = ttk.Combobox(self, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        drop.grid(row = 1, column = 2, columnspan = 2)
        drop.bind('<<ComboboxSelected>>', Button)

        #variable
        duree = StringVar()
        kw = StringVar()
        coef = StringVar()
        self.prix_du_kwh = StringVar()


        #Input labels
        self. kw_input = tk.Entry(self, width = 30, textvariable = kw).grid(row = 2, column = 2, columnspan = 2)
        self.coef_input = tk.Entry(self, width = 30, textvariable = coef).grid(row = 3, column = 2, columnspan = 2)
        self.duree_input = tk.Entry(self, width = 30, textvariable = duree).grid(row = 4, column = 2, columnspan = 2)

        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul_de_prix ).grid(row = 5, column = 3)
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 5, column = 2)
        self.plot_btn = ttk.Button(self,text = "Graphe", command = self.graphe).grid(row = 5, column = 0)
        self.plot_btn_total = ttk.Button(self,text = "Comparaison total", command = Comparaison_kwh).grid(row = 5, column =1)


        #Fonctions
    def Button(self):
        self.kw.set(str(Prix_du_kw[self.drop.get()]))
        self.coef.set(str(Coef_De_Charge[self.drop.get()]))
        self.duree.set(str(Duree_De_Vie[self.drop.get()]))

    def calcul_de_prix(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Error", message = "Please select an energy source!")
        else:
            if(self.kw.get() == ''):
                self.kw.set(str(Prix_du_kw[self.drop.get()]))
            if(self.coef.get() == ''):
                self.coef.set(str(Coef_De_Charge[self.drop.get()]))
            if(self.duree.get() == ''):
                self.duree.set(str(Duree_De_Vie[self.drop.get()]))
            try:
                self.prix_du_kwh.set(str(float(self.kw.get())*100/(365*24*float(self.coef.get())*float(self.duree.get()))))
                prix['text'] = "%.3f cents"%float(self.prix_du_kwh.get())
            except ZeroDivisionError:
                messagebox.showerror('Division par 0', message =  "La durée de vie ne peut pas etre nulle!")

    def reset(self):
        self.drop.set('')
        self.kw.set('')
        self.coef.set('')
        self.duree.set('')

    def graphe(self):
        if(self.prix_du_kwh.get() == ''):
            messagebox.showerror("Erreur", message="Veuillez remplir l'interface!")

        else:
            plot_window = tk.Tk()
            plot_window.title("Prix du KWh actualisé")
            prix_act = float("%.3f" % float(self.prix_du_kwh.get()))
            data = {
                'Fuel-based': self.prix_du_kwh["Fuel-based"],
                self.drop.get(): prix_act
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


       
    def quit_me(self):
        print('quit')
        self.quit()
        self.destroy()
