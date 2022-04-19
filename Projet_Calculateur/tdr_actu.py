from Variables_Fixes import *
from PIL import Image, ImageTk 

class Tdr_actu(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        self.title("Temps De Retour Actualisé")
        self.configure(bg = 'white')

        self.bg = Image.open("bg.png")
        self.bg = ImageTk.PhotoImage(self.bg.resize((800,550), Image.ANTIALIAS))
        self.la = Label(self, image = self.bg)
        self.la.place(x = 0, y = 0)

        #labels
        self.label_KW = Label(self,text = "Le prix du KWh est :", font = 'arial', bg = 'white')
        self.label_KW.grid(row = 1,column = 0, sticky = 'w',padx=30,pady=(0,20))
        self.label = Label(self,text = "Le temps de retour actualisé :", font = 'arial', bg = 'white')
        self.label.grid(row = 7,column = 0, sticky = 'e',columnspan=2)
        self.label_inv = Label(self , text = "Investissement total (en $) : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w',padx=30,pady=(0,20))
        self.label_KW_installed = Label(self , text = "La capacité est : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w',padx=30,pady=(0,20))

        self.prix = Label(self,text = "0.0 année", font = 'arial', fg = 'red', bg = 'white')
        self.prix.grid(row = 7,column = 2, sticky = 'w')

        #ComboBox
        self.select = Label(self,text = "Choisissez votre source d'énergie : ", font = 'arial', bg = 'white').grid(row = 0, column = 0,padx=30,pady=(30,15))
        self.drop = ttk.Combobox(self, width = 47, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        self.drop.grid(row = 0, column = 2, columnspan = 2)
        self.drop.bind('<<ComboboxSelected>>', self.Button)

        #variable
        self.inv = StringVar()
        self.prix_kwh = StringVar()
        self.kw_installed = StringVar()
        self.TR = StringVar()


        #Input labels
        self.inv_input = tk.Entry(self, width = 50, textvariable = self.inv)
        self.inv_input.grid(row = 3, column = 2, columnspan = 2)
        self.kw_input = tk.Entry(self, width = 50, textvariable = self.prix_kwh)
        self.kw_input.grid(row = 1, column = 2, columnspan = 2)
        self.kw_installed_input = tk.Entry(self, width = 50, textvariable = self.kw_installed)
        self.kw_installed_input.grid(row = 2, column = 2, columnspan = 2)

        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul ).grid(row = 6, column = 3,pady=(15,10))
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 6, column = 2,pady=(15,10))
        self.plot_btn = ttk.Button(self,text = "Graphe", command = self.graphe,width=50).grid(row = 8, column = 0,pady=(10,20),columnspan=2)
        self.plot_total_btn = ttk.Button(self,text = "Comparaison", command = Comparaison_TR,width=50).grid(row = 8, column = 2,columnspan=2,pady=(10,20))



    #Fonctions
    def Button(self,event):
        self.kw_input.delete('0',END)
        self.kw_input.insert('0',str(Prix_Du_KWh[self.drop.get()]))
        self.kw_installed_input.delete('0',END)
        self.kw_installed_input.insert('0',str(Capacite[self.drop.get()]))


    def calcul(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Erreur", message = "Choisissez votre source d'énergie! ")
        else:
            self.prix_kwh.set(self.kw_input.get())
            self.inv.set(self.inv_input.get())
            self.kw_installed.set(self.kw_installed_input.get())
            if(self.prix_kwh.get() == ''):
                self.prix_kwh.set(str(Prix_du_kw[self.drop.get()]))
            if(self.kw_installed.get() == ''):
                self.kw_installed.set(str(Capacite[self.drop.get()]))
            if(self.inv.get() == ''):
                messagebox.showerror('Erreur!', message= "Veuillez insérer l'invesstissement ")
            production = float(self.kw_installed.get())*8760*Coef_De_Charge[self.drop.get()]
            gain = production *(Prix_Du_KWh["Fuel-based"] - float(self.prix_kwh.get()))
            facteur = 1- (float(self.inv.get())*(taux_croiss_eco/(1+taux_croiss_eco))/gain)
            if(facteur <0):
                messagebox.showerror("Le temps de retour ne peut pas être calculer!")
                exit(1)
            else:
                self.TR.set(str(log(1-facteur)/log(1/(1+taux_croiss_eco))))
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

 