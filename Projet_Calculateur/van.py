from Variables_Fixes import *
from PIL import Image, ImageTk 

class Van(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        self.title("Valeur actuelle nette")
        self.configure(bg = 'white')
        
        self.bg = Image.open("bg.png")
        self.bg = ImageTk.PhotoImage(self.bg.resize((800,550), Image.ANTIALIAS))
        self.la = Label(self, image = self.bg)
        self.la.place(x = 0, y = 0)

        #labels
        self.label = Label(self,text = "La valeur actuelle nette est", font = 'arial', bg = 'white')
        self.label.grid(row = 7,column = 0, sticky = 'e',columnspan=2)
        self.label_kwh = Label(self , text = "Prix du KWh est (en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w',padx=(70,100),pady=(0,20))
        self.label_taux = Label(self , text = "Le taux d'actualisation est : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w',padx=(70,100),pady=(0,20))
        self.label_inv = Label(self , text = "L'investissement est(en $) : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w',padx=(70,100),pady=(0,20))
        self.label_capacite= Label(self,text= "La capacité installé(en kW) :", font='arial', bg = 'white'). grid(row = 5, column = 0, sticky = 'w',padx=(70,100),pady=(0,20))
        self.valeur = Label(self,text = "0.0$", font = 'arial', fg = 'red', bg = 'white')
        self.valeur.grid(row = 7,column = 2, sticky = 'w')

        #ComboBox
        self.select = Label(self,text = "Choisissez votre source d'énergie : ", font = 'arial', bg = 'white').grid(row = 1, column = 0,sticky='w',padx=(70,100),pady=(30,15))
        self.drop = ttk.Combobox(self, width = 47, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        self.drop.grid(row = 1, column = 2,columnspan=2,pady=(30,15))
        self.drop.bind('<<ComboboxSelected>>', self.Button)

        #variable
        self.inv = StringVar()
        self.kwh = StringVar()
        self.taux = StringVar()
        self.capacite = StringVar()

        #Input labels
        self.kwh_input = tk.Entry(self, textvariable = self.kwh,width=50)
        self.kwh_input.grid(row = 2, column = 2, columnspan = 2,pady=(0,20))
        self.taux_input = tk.Entry(self, textvariable = self.taux,width=50)
        self.taux_input.grid(row = 3, column = 2, columnspan = 2,pady=(0,20))
        self.inv_input = tk.Entry(self, textvariable = self.inv,width=50)
        self.inv_input.grid(row = 4, column = 2, columnspan = 2,pady=(0,20))
        self.capacite_entry=tk.Entry(self, textvariable = self.capacite,width=50)
        self.capacite_entry.grid(row = 5, column = 2, columnspan = 2,pady=(0,20))

        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul_de_prix ).grid(row = 6, column = 3,pady=(0,20))
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 6, column = 2,pady=(0,20))


        #Fonctions
    def Button(self,event):
        self.kwh_input.delete('0',END)
        self.kwh_input.insert('0', str(Prix_Du_KWh[self.drop.get()]))
        self.taux_input.delete('0',END)
        self.taux_input.insert('0', taux_croiss_eco)
        self.inv_input.delete('0',END)
        self.inv_input.insert('0', str(Investissement[self.drop.get()]))
        self.capacite_entry.delete('0',END)
        self.capacite_entry.insert('0',Capacite[self.drop.get()])

    def calcul_de_prix(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Erreur", message = "Choisissez votre source d'énergie!")
        else:
            self.kwh.set(self.kwh_input.get())
            self.taux.set(self.taux_input.get())
            self.inv.set(self.inv_input.get())
            self.capacite.set(self.capacite_entry.get())
            if(self.kwh.get() == ''):
                self.kwh.set(str(Prix_Du_KWh[self.drop.get()]))
            if(self.taux.get() == ''):
                self.taux.set(str(taux_croiss_eco))
            if(self.inv.get() == ''):
                self.inv.set(str(Investissement[self.drop.get()]))
            if(self.capacite.get() == ''):
                messagebox.showerror(title = "Erreur", message = "Veuillez insérer une capacité!")
            try:
                production=float(self.capacite.get())*24*365*Coef_De_Charge[self.drop.get()]
                gain=production*(Prix_Du_KWh["Fuel-based"] - float(self.kwh.get()))
                facteur=(1-(1/(1+float(self.taux.get()))**31))/float(self.taux.get())
                van=gain*facteur-float(self.inv.get())
                if(van < 0):
                    if(self.drop.get() == 'Dechets'):
                        messagebox.showinfo('Attention!', message = "Il faut noter que cette installation résout 2 problèmes différents : électricité et la crise de déchets")
                    else:
                        messagebox.showinfo("Attention!", message="Il faut prendre aussi en considération l'absence d'émssion de CO2")
                self.valeur['text'] = str("%.0f $" %van)
            except ZeroDivisionError:
                messagebox.showerror('Division par 0', message =  "La taux d'actualisation ne peut pas etre nul!")

    def reset(self):
        self.drop.set('')
        self.kwh.set('')
        self.taux.set('')
        self.inv.set('')
        self.capacite.set('')
