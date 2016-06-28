import os, sys
from tkinter import *
import tkinter.ttk as ttk
from Connector import *
from Partie import *
from GameWindow import *
from Interface import *
import ConnWindow as conn

class EndWindow:

    largeur_c = 600
    hauteur_c = 400
    color = "#99693C"

    def __init__(self, container, partie):
        self.container = container
        self.partie = partie
        self.cadre = Frame(container.canvas,
                            bg=self.color)

        self.canvas = Canvas(self.cadre,
                                bg=self.color,
                                width=self.largeur_c,
                                height = self.hauteur_c)

        self.labelPlayer= Label(self.canvas,
                                    text="Nom du joueur :",
                                    bg=self.color)

        self.labelTheme = Label(self.canvas,
                                    text="Thème choisi :",
                                    bg=self.color)

        self.resultat = StringVar()
        self.labelResultat = Label(self.canvas,
                                        text=self.resultat,
                                        bg=self.color)


        self.button = Button(self.canvas,
                                text="Valider",
                                command=self.click)
        self.place_window()
        self.place_elements()
        self.canvas.pack()

    def afficher_resultat(self):
        self.resultat.set("Votre résultat est de  : ", self.partie.calculate_score())

    def place_window(self):
        self.cadre.place(width=self.largeur_c,
                    height=self.hauteur_c,
                    relx=0.5,
                    rely=0.5,
                    anchor=CENTER)

    def place_elements(self):
        self.labelPlayer.place(x=80,
                                y=155,
                                width=200,
                                height=30)

        self.labelTheme.place(x=80,
                                y=205,
                                width=200,
                                height=30)


        self.button.place(relx=0.5,
                            y=280,
                            anchor=CENTER,
                            width=150,
                            height=30)

        self.labelResultat.place(relx=0.5,
                            rely=0.5,
                            anchor=CENTER,
                            width=200,
                            height=30)

    def click(self):
        self.canvas.pack_forget()
        self.interface.changeWin(conn.ConnWindow(self.interface))
