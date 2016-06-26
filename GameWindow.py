import os, sys
from tkinter import *
import tkinter.ttk as ttk
from Connector import *
from Partie import *
from Question1 import *

class GameWindow:

    largeur_c = 600
    hauteur_c = 400
    color = "#99693C"


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
        content = Connector.get_themes_db()
        self.question1 = Question1()
        self.container = container
        self.cadre = Frame(container.canvas,
                            bg=self.color)

        self.canvas = Canvas(self.cadre,
                                bg=self.color,
                                width=self.largeur_c,
                                height = self.hauteur_c)

        self.labelquestionNumber = Label(self.canvas,
                                    text=self.createNumberMessage(self.question1.number),
                                    bg=self.color)

        self.labelQuestion= Label(self.canvas,
                                    text=self.question1.text,
                                    bg=self.color)

        self.button1 = Button(self.canvas,
                                text=self.question1.reponseList[0],
                                command=self.click)

        self.button2 = Button(self.canvas,
                                text=self.question1.reponseList[1],
                                command=self.click)

        self.button3 = Button(self.canvas,
                                text=self.question1.reponseList[2],
                                command=self.click)

        self.button4 = Button(self.canvas,
                                text=self.question1.bonneReponse,
                                command=self.click)

        self.place_elements()
        self.place_window()
        self.canvas.pack()
        print ("yes")

    def place_window(self):
        self.cadre.place(width=self.largeur_c,
                    height=self.hauteur_c,
                    relx=0.5,
                    rely=0.5,
                    anchor=CENTER)


    def place_elements(self):
        self.labelquestionNumber.place(x=100,
                                y=25,
                                width=400,
                                height=30)

        self.labelQuestion.place(x=100,
                                y=75,
                                width=400,
                                height=100)

        self.button1.place(relx=0.33,
                            y=200,
                            anchor=CENTER,
                            width=200,
                            height=30)

        self.button2.place(relx=0.66,
                            y=200,
                            anchor=CENTER,
                            width=200,
                            height=30)

        self.button3.place(relx=0.33,
                            y=280,
                            anchor=CENTER,
                            width=200,
                            height=30)

        self.button4.place(relx=0.66,
                            y=280,
                            anchor=CENTER,
                            width=200,
                            height=30)

    def click(self):
        self.destroy()


    def createNumberMessage(self, number):
        messages = ['Première Question, !', 'Deuxième Question, on se donne à fond !', 'Ne vous déconcentrez pas !', 'Quatrième Question !', 'Cinquième Question, vous arrivez à suivre ?', 'Sixième Question !', 'Septième Question !', 'Huitième Question, pas loin de la fin !', 'Neuvième Question ! ', 'Et la Dixième !']
        return messages[number]
