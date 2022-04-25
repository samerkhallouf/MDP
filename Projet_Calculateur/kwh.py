from Variables_Fixes import *
from PIL import Image, ImageTk 

class Kwh(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Prix du KWh")
        self.geometry("800x550")
        self.configure(bg = 'white')

        self.bg = Image.open("bg.png")
        self.bg = ImageTk.PhotoImage(self.bg.resize((800,550), Image.ANTIALIAS))
        self.la = Label(self, image = self.bg)
        self.la.place(x = 0, y = 0)

        #labels
        label = Label(self,text = "Le prix du KWh est :", font = 'arial', bg = 'white')
        label.grid(row = 6,column = 0, sticky = 'e',columnspan=2)
        self.label_kw = Label(self , text = "Prix du KW est(en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w',padx=(70,100),pady=(0,20))
        self.label_coef = Label(self , text = "Coefficient de charge : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w',padx=(70,100),pady=(0,20))
        self.label_duree = Label(self , text = "La duree de vie (en année) : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w',padx=(70,100),pady=(0,20))
        self.prix = Label(self,text = "0.0 cents", font = 'arial', fg = 'red', bg = 'white')
        self.prix.grid(row = 6,column = 2, sticky = 'w')

         #ComboBox
        self.select = Label(self,text = "Choisissez votre source d'énergie : ", font = 'arial', bg = 'white').grid(row = 1, column = 0,padx=(70,100),pady=(30,15))
        self.drop = ttk.Combobox(self, width = 47, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        self.drop.grid(row = 1, column = 2, columnspan = 2)
        self.drop.bind('<<ComboboxSelected>>', self.Button)

        #variable
        self.duree = tk.StringVar()
        self.kw = tk.StringVar()
        self.coef = tk.StringVar()
        self.prix_du_kwh = tk.StringVar()
        self.duree.set('')
        self.kw.set('')
        self.coef.set('')
        self.prix_du_kwh.set('')


        #Input labels
        self.kw_input = Entry(self, width = 50, textvariable = self.kw)
        self.kw_input.grid(row = 2, column = 2, columnspan = 2)
        self.coef_input = Entry(self, width = 50, textvariable = self.coef)
        self.coef_input.grid(row = 3, column = 2, columnspan = 2)
        self.duree_input = Entry(self, width = 50, textvariable = self.duree)
        self.duree_input.grid(row = 4, column = 2, columnspan = 2)


        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul_de_prix ).grid(row = 5, column = 3,pady=(15,10))
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 5, column = 2,pady=(15,10))
        self.plot_btn = ttk.Button(self,text = "Graphe", command = self.graphe,width=50).grid(row = 7, column = 0,pady=(10,20),columnspan=2)
        self.plot_total_btn = ttk.Button(self,text = "Comparaison totale", command = Comparaison_kwh,width=50).grid(row = 7, column = 2,columnspan=2,pady=(10,20))



        #Fonctions
    def Button(self,event):
        self.kw_input.delete('0',tk.END)
        self.kw_input.insert('0',str(Prix_du_kw[self.drop.get()]))
        self.coef_input.delete('0',tk.END)
        self.coef_input.insert('0',str(Coef_De_Charge[self.drop.get()]))
        self.duree_input.delete('0',tk.END)
        self.duree_input.insert('0',str(Duree_De_Vie[self.drop.get()]))

    def calcul_de_prix(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Erreur", message = "Choisissez votre source d'énergie")
        else:
            self.kw.set(self.kw_input.get())
            self.coef.set(self.coef_input.get())
            self.duree.set(self.duree_input.get())
            if(self.kw.get() == ''):
                self.kw.set(str(Prix_du_kw[self.drop.get()]))
            if(self.coef.get() == ''):
                self.coef.set(str(Coef_De_Charge[self.drop.get()]))
            if(self.duree.get() == ''):
                self.duree.set(str(Duree_De_Vie[self.drop.get()]))
            try:
                self.prix_du_kwh.set(str(float(self.kw.get())*100/(365*24*float(self.coef.get())*float(self.duree.get()))))
                self.prix['text'] = "%.3f cents"%float(self.prix_du_kwh.get())
            except ZeroDivisionError:
                messagebox.showerror('Division par 0', message =  "La durée de vie ne peut pas etre nulle!")

    def reset(self):
        self.drop.set('')
        self.kw.set('')
        self.coef.set('')
        self.duree.set('')
        self.prix["text"] = "0.0 cents"

    def graphe(self):
        if(self.prix_du_kwh.get() == ''):
            messagebox.showerror("Erreur", message="Veuillez remplir l'interface!")

        else:
            plot_window = tk.Tk()
            plot_window.title("Prix du KWh actualisé")
            prix_act = float("%.3f" % float(self.prix_du_kwh.get()))
            data = {
                'Fuel-based': Prix_Du_KWh["Fuel-based"],
                self.drop.get(): prix_act/100
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
            axes.set_ylabel('Cout(en $)')

            figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


       

