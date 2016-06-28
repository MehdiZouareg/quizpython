import os, sys
from tkinter import *
import tkinter.ttk as ttk
from Connector import *
from Partie import *
from GameWindow import *
from Interface import *
from EndWindow import *

class ConnWindow:


    LARGEUR_C = 600
    HAUTEUR_C = 400
    COLOR = "#90C3D4"

    """                                 """
    """     Attributs : Connexion       """
    """                                 """
    themesContent = []

    """                     """
    """     Constructeur    """
    """                     """

    def __init__(self, container):
        #Attributs liés à la fenêtre
        self.themesContent = []
        self.container = container
        self.cadre = Frame(container.canvas,
                            bg=self.COLOR)
        self.canvas = Canvas(self.cadre,
                                bg=self.COLOR,
                                width=self.LARGEUR_C,
                                height=self.HAUTEUR_C)
        #Labels
        self.labelWelcome = Label(self.canvas,
                                    text="Bienvenue dans le Quizz !",
                                    bg=self.COLOR)
        self.labelPlayer= Label(self.canvas,
                                    text="Nom du joueur :",
                                    bg=self.COLOR)
        self.labelTheme = Label(self.canvas,
                                      text="Thème choisi :",
                                      bg=self.COLOR)
        self.labelAddTheme = Label(self.canvas,
                                    text="Ajouter un thème :",
                                    bg=self.COLOR)
        self.labelAddQuestion = Label(self.canvas,
                                    text="Ajouter une question :",
                                    bg=self.COLOR)
        self.labelAddBonneReponse = Label(self.canvas,
                                    text="Ajouter la bonne réponse :",
                                    bg=self.COLOR)
        self.labelAddReponse1 = Label(self.canvas,
                                    text="Ajouter le choix 2:",
                                    bg=self.COLOR)
        self.labelAddReponse2 = Label(self.canvas,
                                    text="Ajouter le choix 3:",
                                    bg=self.COLOR)
        self.labelAddReponse3 = Label(self.canvas,
                                    text="Ajouter le choix 4:",
                                    bg=self.COLOR)
        self.labelAddThemeQuest = Label(self.canvas,
                                            text="Attribuer un thème :",
                                            bg=self.COLOR)
        #Valeurs
        self.valueTextUser = StringVar()
        self.valueTextAddTheme = StringVar()
        self.valueTextAddQuestion = StringVar()
        self.valueTextAddBonneReponse = StringVar()
        self.valueTextAddReponse1 = StringVar()
        self.valueTextAddReponse2 = StringVar()
        self.valueTextAddReponse3 = StringVar()
        self.valueTheme = StringVar()
        #Textbox thème
        themes = Connector.get_themes_db()
        for elem in themes:
            self.themesContent.append(str(elem[0]))
        self.listBoxTheme = ttk.Combobox(self.canvas,
                                        textvariable=self.valueTheme,
                                        values=self.themesContent)
        self.textBoxUser = Entry(self.canvas,
                                    textvariable = self.valueTextUser)
        self.textBoxAddTheme = Entry(self.canvas,
                                    textvariable = self.valueTextAddTheme)
        self.textBoxAddQuestion = Entry(self.canvas,
                                        textvariable = self.valueTextAddQuestion)
        self.textBoxAddBonneReponse = Entry(self.canvas,
                                        textvariable = self.valueTextAddBonneReponse)
        self.textBoxAddReponse1 = Entry(self.canvas,
                                    textvariable = self.valueTextAddReponse1)
        self.textBoxAddReponse2 = Entry(self.canvas,
                                    textvariable = self.valueTextAddReponse2)
        self.textBoxAddReponse3 = Entry(self.canvas,
                                    textvariable = self.valueTextAddReponse3)
        #Boutons
        self.buttonValid = Button(self.canvas,
                                    text="Valider",
                                    command=self.launch_partie)
        self.buttonAddContent = Button(self.canvas,
                                        text="Ajouter Contenu",
                                        command=self.add_content)
        self.buttonAddTheme = Button(self.canvas,
                                        text="Ajouter Thème",
                                        command=self.add_theme)
        self.buttonAddQuestion = Button(self.canvas,
                                        text="Ajouter Question",
                                        command=self.add_question)
        #Placement de la fenêtre et des widgets de connexion
        self.place_window()
        self.place_elements_id()
        self.canvas.pack()



    def place_window(self):
        """     Placement de la fenêtre """
        self.cadre.place(width=self.LARGEUR_C,
                    height=self.HAUTEUR_C,
                    relx=0.5,
                    rely=0.5,
                    anchor=CENTER)



    def place_elements_id(self):
        """ Placement des widgets de connexion """
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
        self.buttonValid.place(relx=0.5,
                            y=280,
                            anchor=CENTER,
                            width=150,
                            height=30)
        self.buttonAddContent.place(relx=0.5,
                                        y=330,
                                        anchor=CENTER,
                                        width=150,
                                        height=30)

    def place_elements_content(self):
        """ Placement des widgets d'ajout de contenu """
        #Ajouter un thème
        self.labelAddTheme.place(relx=0.5,
                                    y=25,
                                    anchor=CENTER,
                                    width=200,
                                    height=30)
        self.textBoxAddTheme.place(relx=0.5,
                                    y=55,
                                    anchor=CENTER,
                                    width=300,
                                    height=30)
        self.buttonAddTheme.place(relx=0.5,
                                    y=95,
                                    anchor=CENTER,
                                    width=150,
                                    height=30)
        #Ajouter une question
        self.labelAddQuestion.place(relx=0.5,
                                        y=140,
                                        anchor=CENTER,
                                        width=200,
                                        height=30)
        self.textBoxAddQuestion.place(relx=0.5,
                                        y=170,
                                        anchor=CENTER,
                                        width=300,
                                        height=30)
        self.labelAddBonneReponse.place(x=80,
                                         y=200,
                                         width=200,
                                         height=20)
        self.textBoxAddBonneReponse.place(x=300,
                                            y=195,
                                            width=200,
                                            height=20)
        self.labelAddReponse1.place(x=80,
                                    y=225,
                                    width=200,
                                    height=20)
        self.textBoxAddReponse1.place(x=300,
                                        y=225,
                                        width=200,
                                        height=20)
        self.labelAddReponse2.place(x=80,
                                    y=255,
                                    width=200,
                                    height=20)
        self.textBoxAddReponse2.place(x=300,
                                        y=255,
                                        width=200,
                                        height=20)
        self.labelAddReponse3.place(x=80,
                                    y=285,
                                    width=200,
                                    height=20)
        self.textBoxAddReponse3.place(x=300,
                                        y=285,
                                        width=200,
                                        height=20)
        self.labelAddThemeQuest.place(x=80,
                                        y=315,
                                        width=200,
                                        height=20)
        self.listBoxTheme.place(x=300,
                                y=315,
                                width=200,
                                height=20)
        self.buttonAddQuestion.place(relx=0.5,
                                        y=360,
                                        anchor=CENTER,
                                        width=150,
                                        height=30)

    def hide_elements_id(self):
        """ Cacher les widgets de connexion """
        self.labelWelcome.place_forget()
        self.labelPlayer.place_forget()
        self.labelTheme.place_forget()
        self.textBoxUser.place_forget()
        self.listBoxTheme.place_forget()
        self.buttonValid.place_forget()
        self.buttonAddContent.place_forget()

    def hide_elements_content(self):
        """ Cacher les widgets d'ajout de contenu """
        self.labelAddTheme.place_forget()
        self.labelAddQuestion.place_forget()
        self.labelAddBonneReponse.place_forget()
        self.labelAddReponse1.place_forget()
        self.labelAddReponse2.place_forget()
        self.labelAddReponse3.place_forget()
        self.labelAddThemeQuest.place_forget()
        self.textBoxAddTheme.place_forget()
        self.textBoxAddQuestion.place_forget()
        self.textBoxAddBonneReponse.place_forget()
        self.textBoxAddReponse1.place_forget()
        self.textBoxAddReponse2.place_forget()
        self.textBoxAddReponse3.place_forget()
        self.listBoxTheme.place_forget()
        self.buttonAddTheme.place_forget()
        self.buttonAddQuestion.place_forget()


    def launch_partie(self):
        """Lancer la partie """
        self.canvas.pack_forget()
        self.themeChoisi = str(self.valueTheme.get())
        self.joueur = str(self.valueTextUser.get())
        self.partie = Partie(self.themeChoisi, self.joueur)
        self.partie.new_game(self.container)

    def add_content(self):
        """ Lancer mode ajout de contenu """
        self.hide_elements_id()
        self.place_elements_content()

    def add_theme(self):
        """ Ajouter thème dans bdd """
        themeToSend = str(self.valueTextAddTheme.get())
        if themeToSend:
            Connector.add_theme(themeToSend)
            self.textBoxAddTheme.delete(0,END)
            self.themesContent = Connector.get_themes_db()
            self.delete_form()
            self.hide_elements_content()
            self.place_elements_id()

    def add_question(self):
        """ Ajouter question dans bdd """
        test = True
        dict = {'id':None,
                'quest':self.valueTextAddQuestion.get(),
                'brep':self.valueTextAddBonneReponse.get(),
                'rep1':self.valueTextAddReponse1.get(),
                'rep2':self.valueTextAddReponse2.get(),
                'rep3':self.valueTextAddReponse3.get(),
                'theme':self.valueTheme.get()}
        for cle, oc in dict.items():
            if cle != 'id' and not oc:
                test = False
        if test:
            Connector.add_question(dict)
            self.themesContent = Connector.get_themes_db()
            self.delete_form()
            self.hide_elements_content()
            self.place_elements_id()

    def delete_form(self):
        """ Efface tous les formulaires de la page """
        self.listBoxTheme.delete(0,END)
        self.textBoxAddTheme.delete(0,END)
        self.textBoxUser.delete(0,END)
        self.textBoxAddQuestion.delete(0,END)
        self.textBoxAddBonneReponse.delete(0,END)
        self.textBoxAddReponse1.delete(0,END)
        self.textBoxAddReponse2.delete(0,END)
        self.textBoxAddReponse3.delete(0,END)
