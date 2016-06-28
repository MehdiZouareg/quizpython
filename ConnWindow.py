import os, sys
from tkinter import *
import tkinter.ttk as ttk
from Connector import *
from Partie import *
from GameWindow import *
from Interface import *

class ConnWindow:

    largeur_c = 600
    hauteur_c = 400
    color = "#90C3D4"

    container = None
    cadre = None
    canvas = None

    labelWelcome = None
    labelPlayer = None
    labelTheme = None
    textBoxUser = None
    listBoxTheme = None
    button = None

    valueTextUser = None
    valueThemes = None

    def __init__(self, container):
        self.container = container
        self.cadre = Frame(container.canvas,
                            bg=self.color)

        self.canvas = Canvas(self.cadre,
                                bg=self.color,
                                width=self.largeur_c,
                                height = self.hauteur_c)

        self.labelWelcome = Label(self.canvas,
                                    text="Bienvenue dans le Quizz !",
                                    bg=self.color)

        self.labelPlayer= Label(self.canvas,
                                    text="Nom du joueur :",
                                    bg=self.color)

        self.labelTheme = Label(self.canvas,
                                    text="Thème choisi :",
                                    bg=self.color)


        self.valueTextUser = StringVar()
        self.textBoxUser = Entry(self.canvas,
                                    textvariable = self.valueTextUser)

        self.valueTheme = StringVar()
        content = Connector.get_themes_db()
        self.listBoxTheme = ttk.Combobox(self.canvas,
                                        textvariable=self.valueTheme,
                                        values=content)

        self.button = Button(self.canvas,
                                text="Valider",
                                command=self.click)
        self.place_window()
        self.place_elements()
        self.canvas.pack()




    def place_window(self):
        self.cadre.place(width=self.largeur_c,
                    height=self.hauteur_c,
                    relx=0.5,
                    rely=0.5,
                    anchor=CENTER)



    def place_elements(self):
        self.labelWelcome.place(relx=0.5,
                                y=100,
                                anchor=CENTER,
                                width=200,
                                height=30)

        self.labelPlayer.place(x=80,
                                y=155,
                                width=200,
                                height=30)

        self.labelTheme.place(x=80,
                                y=205,
                                width=200,
                                height=30)

        self.textBoxUser.place(x=250,
                                y=150,
                                width=200,
                                height=30)

        self.listBoxTheme.place(x=250,
                                y=200,
                                width=200,
                                height=30)

        self.button.place(relx=0.5,
                            y=280,
                            anchor=CENTER,
                            width=150,
                            height=30)

    def click(self):
        self.canvas.pack_forget()
        self.partie = Partie(self.valueTextUser, self.valueTheme)
        self.partie.new_game(self.container)
