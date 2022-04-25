from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from math import log
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)



Coef_De_Charge = {'Photovoltaique':0.17, 'CSP': 0.75, 'Dechets':0.90, 'Eolienne offshore': 0.5}
Prix_du_kw = {'Photovoltaique':1400, 'CSP': 11000, 'Dechets':15300, 'Eolienne offshore':8000}
Duree_De_Vie = {'Photovoltaique':25, 'CSP': 30, 'Dechets':12.5, 'Eolienne offshore':17}
Investissement = {'Photovoltaique':3990000000, 'CSP': 222000000, 'Dechets':3014000000, 'Eolienne offshore':2000000000}
Prix_Du_KWh = {'Photovoltaique':0.035, 'CSP': 0.056, 'Dechets':0.155, 'Eolienne offshore':0.107, "Fuel-based":0.24, "Gaz naturel" : 0.15}
Prix_Du_KWh_act = {'Photovoltaique': 35, 'CSP': 86.5, 'Dechets':0.155, 'Eolienne offshore':102, "Fuel-based":0.24}
Capacite = {'Photovoltaique':2850000, 'CSP': 20000, 'Dechets':197000, 'Eolienne offshore':250000}
taux_croiss_eco = 0.1
Emission_CO2 = {'Photovoltaique':0.032, 'CSP': 0.032, 'Dechets':0.03, 'Eolienne offshore':0.001,"Heavy-Fuel":0.778,"Diesel oil":0.778,"Natural Gas":0.443,"Hydro":0.01}
Temps_de_retour = {'Photovoltaique':5.7, 'CSP': 30.2, 'Dechets':12, 'Eolienne offshore':19.6}

def Comparaison_kwh():
    plot_window = tk.Tk()
    plot_window.geometry("850x330")
    plot_window.title("Prix du KWh de toutes les technologies")
    energies = Prix_Du_KWh.keys()
    cout = Prix_Du_KWh.values()

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
    axes.set_title('Prix du KWh')
    axes.set_ylabel('Cout(en $)')

    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def Comparaison_kwh_act():
    plot_window = tk.Tk()
    plot_window.geometry("850x330")
    plot_window.title("Prix du KWh actualisé de toutes les technologies")
    energies = Prix_Du_KWh_act.keys()
    cout = Prix_Du_KWh_act.values()

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
    axes.set_ylabel('Cout(en cents)')

    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def Comparaison_CO2():
    plot_window = tk.Tk()
    plot_window.title("Empreinte de CO2 de toutes les technologies")
    plot_window.geometry("1080x330")
    energies = Emission_CO2.keys()
    cout = Emission_CO2.values()

    # create a figure
    figure = Figure(figsize=(6, 4), dpi=100)

    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure, plot_window)

    # create the toolbar
    NavigationToolbar2Tk(figure_canvas, plot_window)

    # create axes
    axes = figure.add_subplot()

    # create the barchart
    axes.bar(energies, cout, color = ["green","green","green","green","red","red","yellow","green"])
    axes.set_title('Empreinte de CO2')
    axes.set_ylabel('Empreinte (Tonnes/MWh produits)')

    figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def Comparaison_TR():
        plot_window = tk.Tk()
        plot_window.title("Temps de retour de toutes les technologies")
        plot_window.geometry("1080x330")
        energies = Temps_de_retour.keys()
        cout = Temps_de_retour.values()

        # create a figure
        figure = Figure(figsize=(6, 4), dpi=100)

        # create FigureCanvasTkAgg object
        figure_canvas = FigureCanvasTkAgg(figure, plot_window)

        # create the toolbar
        NavigationToolbar2Tk(figure_canvas, plot_window)

        # create axes
        axes = figure.add_subplot()

        # create the barchart
        axes.bar(energies, cout, color=["green", "green", "green", "green", "red", "red", "yellow", "green"])
        axes.set_title('Temps de retour')
        axes.set_ylabel('Année(s)')

        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)