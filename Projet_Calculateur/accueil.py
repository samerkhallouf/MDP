from tkinter import *
import tkinter as tk
from van import *
from prix import *
from co2 import *
from temp import *
from PIL import Image, ImageTk


def window_van():
    Van()

def window_temp():
    Temp()

def window_prix():
    Prix()

def window_co2():
    Co2()

#Root window:
root = tk.Tk()
w = root.winfo_height
root.geometry("800x550")
root.title("Accueil")
root.configure(bg = 'white')

label = Label(root,text = "Que voulez-vous calculer? ", font = ('arial',24), bg = 'white')
label.grid(row = 1,column = 2,columnspan=2,pady=(50,0))

img1= Image.open("image1.png")
img1 = ImageTk.PhotoImage(img1.resize((150,150), Image.ANTIALIAS))
image_kwh = Button(root, image = img1,command=window_prix)
image_kwh.grid(row = 2,column = 1, padx=20,pady=(50,10))
label1 = Label(root,text = "Prix du kwh", font = 'arial', bg = 'white')
label1.grid(row = 3,column = 1)

img2= Image.open("image2.png")
img2 = ImageTk.PhotoImage(img2.resize((150,150), Image.ANTIALIAS))
image_tdr = Button(root, image = img2,command=window_temp)
image_tdr.grid(row = 2,column = 2, pady=(50,10),padx=20)
label2 = Label(root,text = "Temps de retour", font = 'arial', bg = 'white')
label2.grid(row = 3,column = 2)

img3= Image.open("image3.png")
img3 = ImageTk.PhotoImage(img3.resize((150,150), Image.ANTIALIAS))
image_van = Button(root, image = img3,command=window_van)
image_van.grid(row = 2,column = 3, pady=(50,10),padx=20)
label3 = Label(root,text = "Valeur actuelle nette", font = 'arial', bg = 'white')
label3.grid(row = 3,column = 3)

img4= Image.open("image4.png")
img4 = ImageTk.PhotoImage(img4.resize((150,150), Image.ANTIALIAS))
image_co2 = Button(root, image = img4, command=window_co2)
image_co2.grid(row = 2,column = 4, pady=(50,10), padx=20)
label4 = Label(root,text = "Emission CO2", font = 'arial', bg = 'white')
label4.grid(row = 3,column = 4)

def quit_me():
    print('quit')
    root.quit()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", quit_me)

root.mainloop()