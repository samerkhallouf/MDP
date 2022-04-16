from Variables_Fixes import *

class Van(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("550x200")
        self.title("Valeur actuelle nette")
        self.configure(bg = 'white')
        self.protocol("WM_DELETE_WINDOW", self.quit_me)

        #labels
        self.label = Label(self,text = "La valeur actuelle nette est", font = 'arial', bg = 'white')
        self.label.grid(row = 7,column = 0, sticky = 'e')
        self.label_kwh = Label(self , text = "Prix du KWh est (en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')
        self.label_taux = Label(self , text = "Le taux de croissance économique est : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
        self.label_inv = Label(self , text = "L'investissement est : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w')
        self.label_capacite= Label(self,text= "La capacité installé:", font='arial', bg = 'white'). grid(row = 5, column = 0, sticky = 'w')
        self.valeur = Label(self,text = "0.0$", font = 'arial', fg = 'red', bg = 'white')
        self.valeur.grid(row = 7,column = 2, sticky = 'w')

                #ComboBox
        self.select = Label(self,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 1, column = 0,sticky='w')
        self.drop = ttk.Combobox(self, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
        self.drop.grid(row = 1, column = 2, columnspan = 2)
        self.drop.bind('<<ComboboxSelected>>', Button)

        #variable
        inv = StringVar()
        kwh = StringVar()
        taux = StringVar()
        capacite = StringVar()

        #Input labels
        self.kwh_input = tk.Entry(self, width = 30, textvariable = kwh).grid(row = 2, column = 2, columnspan = 2)
        self.taux_input = tk.Entry(self, width = 30, textvariable = taux).grid(row = 3, column = 2, columnspan = 2)
        self.inv_input = tk.Entry(self, width = 30, textvariable = inv).grid(row = 4, column = 2, columnspan = 2)
        self.capacite_entry=tk.Entry(self, width = 30, textvariable = capacite).grid(row = 5, column = 2, columnspan = 2)

        #buttons
        self.button = ttk.Button( self , text = "Calcul", command = self.calcul_de_prix ).grid(row = 6, column = 3)
        self.reset_btn = ttk.Button(self, text = "Reset", command = self.reset).grid(row = 6, column = 2)


        #Fonctions
    def Button(self):
        self.kwh.set(str(Prix_Du_KWh[self.drop.get()]))
        self.taux.set(taux_croiss_eco)
        self.inv.set(str(Investissement[self.drop.get()]))


    def calcul_de_prix(self):
        if(self.drop.get() == ''):
            messagebox.showerror(title = "Error", message = "Please select an energy source!")
        else:
            if(self.kwh.get() == ''):
                self.kwh.set(str(Prix_Du_KWh[self.drop.get()]))
            if(self.taux.get() == ''):
                self.taux.set(str(taux_croiss_eco))
            if(self.inv.get() == ''):
                self.inv.set(str(Investissement[self.drop.get()]))
            if(self.capacite.get() == ''):
                messagebox.showerror(title = "Error", message = "Please enter a capacity!")
            try:
                production=float(self.capacite.get())*24*365*Coef_De_Charge[self.drop.get()]
                gain=production*(Prix_Du_KWh["Fuel-based"] - float(self.kwh.get()))
                facteur=(1-(1/(1+float(self.taux.get()))**31))/float(self.taux.get())
                van=gain*facteur-float(self.inv.get())
                self.valeur['text'] = str("%.3f" %van)
            except ZeroDivisionError:
                messagebox.showerror('Division par 0', message =  "La taux de croissance économique ne peut pas etre nul!")

    def reset(self):
        self.drop.set('')
        self.kwh.set('')
        self.taux.set('')
        self.inv.set('')
        self.capacite.set('')
    
    def quit_me(self):
        print('quit')
        self.quit()
        self.destroy()



if __name__ == "__main__":
    app = Van()
    app.mainloop()

