from tkinter import *
import tkinter as tk
from kwh import *
from kwh_actu import *

class Prix(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        self.title("Accueil")
        self.configure(bg = 'white')
        self.protocol("WM_DELETE_WINDOW", self.quit_me)

        self.label = Label(self,text = "Choisissez:", font = ('arial',24), bg = 'white')
        self.label.grid(row = 1,column=0,columnspan=2,pady=50,padx=220)


        self.button1 = Button(self,text = "                   Prix du KWh                    ", font = 'arial', bg = 'white',command=self.window_kwh)
        self.button1.grid(row = 2,column = 0,pady=20,padx=220)


        self.button2 = Button(self,text = "             Prix du KWh actualisé            ", font = 'arial', bg = 'white',command=self.window_kwh_actu)
        self.button2.grid(row = 3,column = 0,pady=20,padx=220)


    def window_kwh(self):
        self.withdraw()
        Kwh()
    
    def window_kwh_actu(self):
        self.withdraw()
        Kwh_actu()

    def quit_me(self):
        print('quit')
        self.quit()
        self.destroy()



