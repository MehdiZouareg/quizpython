import os, sys
from tkinter import *
import tkinter.ttk as ttk
from Connector import *
from Partie import *
from Question1 import *

class GameWindow:

    largeur_c = 600
    hauteur_c = 400
    color = "#A1D490"


    container = None
    cadre = None
    canvas = None

    labelWelcome = None
    labelPlayer = None
    labelTheme = None
    textBoxUser = None
    listBoxTheme = None
    button1 = None
    button2 = None
    button3 = None
    button4 = None
    valueTextUser = None
    valueThemes = None

    def __init__(self, container, nomJoueur, theme, partie, question):
        self.partie = partie
        self.question = question
        self.container = container
        self.nomJoueur = str(partie.joueur)
        self.nomTheme = str(partie.theme)


        """Eléments de la page Question"""
        self.cadre = Frame(container.canvas,
                            bg=self.color)

        self.canvas = Canvas(self.cadre,
                                bg=self.color,
                                width=self.largeur_c,
                                height = self.hauteur_c)

        self.labelquestionNumber = Label(self.canvas,
                                    text=self.createNumberMessage(self.partie.tour),
                                    bg=self.color)

        self.labelJoueur = Label(self.canvas,
                                text="Joueur :" + self.nomJoueur,
                                bg=self.color)

        self.labelTheme = Label(self.canvas,
                                text="Thème :" + self.nomTheme,
                                bg=self.color)

        self.labelQuestion= Label(self.canvas,
                                    text=self.question.text,
                                    bg=self.color)

        self.button1 = Button(self.canvas,
                                text=self.question.reponseList[0],
                                command= lambda : self.click(self.question.reponseList[0]))

        self.button2 = Button(self.canvas,
                                text=self.question.reponseList[1],
                                command= lambda : self.click(self.question.reponseList[1]))

        self.button3 = Button(self.canvas,
                                text=self.question.reponseList[2],
                                command= lambda : self.click(self.question.reponseList[2]))

        self.button4 = Button(self.canvas,
                                text=self.question.bonneReponse[3],
                                command= lambda : self.click(self.question.reponseList[3]))

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
                                y=50,
                                width=400,
                                height=100)

        self.labelJoueur.place(x=10,
                                y=10,
                                width=100,
                                height=50)

        self.labelTheme.place(x=10,
                                y=300,
                                width=100,
                                height=50)

        self.button1.place(relx=0.30,
                            y=200,
                            anchor=CENTER,
                            width=200,
                            height=50)


        self.button2.place(relx=0.70,
                            y=200,
                            anchor=CENTER,
                            width=200,
                            height=50)


        self.button3.place(relx=0.30,
                            y=280,
                            anchor=CENTER,
                            width=200,
                            height=50)


        self.button4.place(relx=0.70,
                            y=280,
                            anchor=CENTER,
                            width=200,
                            height=50)

    def click(self,reponse):
        self.canvas.pack_forget()
        self.partie.next_turn(reponse, self.question)
        """ Numero de la reponse renvoyée"""


    def createNumberMessage(self, number):
        messages = ['Première Question, !', 'Deuxième Question, on se donne à fond !', 'Ne vous déconcentrez pas !', 'Quatrième Question !', 'Cinquième Question, vous arrivez à suivre ?', 'Sixième Question !', 'Septième Question !', 'Huitième Question, pas loin de la fin !', 'Neuvième Question ! ', 'Et la Dixième !']
        return messages[number]
