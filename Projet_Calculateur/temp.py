from tkinter import *
import tkinter as tk
from tdr import *
from tdr_actu import *

class Temp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x550")
        self.title("Temps de retour")
        self.configure(bg = 'white')

        self.label = Label(self,text = "Choisissez:", font = ('arial',24), bg = 'white')
        self.label.grid(row = 1,column=0,columnspan=2,pady=50,padx=220)


        self.button1 = Button(self,text = "                   Temps de retour                    ", font = 'arial', bg = 'white',command=self.window_tdr)
        self.button1.grid(row = 2,column = 0,pady=20,padx=220)


        self.button2 = Button(self,text = "             Temps de retour actualisé            ", font = 'arial', bg = 'white',command=self.window_tdr_actu)
        self.button2.grid(row = 3,column = 0,pady=20,padx=220)


    def window_tdr(self):
        self.withdraw()
        Tdr()
    
    def window_tdr_actu(self):
        self.withdraw()
        Tdr_actu()

  



