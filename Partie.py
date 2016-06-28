import os, sys
import random
from random import *
from Connector import *
from Question import *
from Interface import *
from GameWindow import *
from EndWindow import *

class Partie:
    """
        La classe métier de base, celle qui contient toutes les autres.
        Représente le déroulement d'un quizz.
    """

    #Le nombre de questions de la partie
    SIZE_PARTIE = 10
    answers = []

    """ CONSTRUCTOR """
    def __init__(self, theme, joueur):
        self.listQuestion = []
        self.joueur = joueur
        self.theme = theme
        print(theme)
        self.questions = Connector.get_questions_db(theme)
        size = len(self.questions) - 1
        for i in range(self.SIZE_PARTIE):
            self.nextQuest = None
            rand = randint(0, size)
            self.nextQuest = Question(self.questions[i])
            self.listQuestion.append(self.nextQuest)
            print("ici!")

    """ Début de la partie. """
    def new_game(self, container):
        self.tour = 0
        self.question = self.listQuestion[self.tour]
        self.container = container
        self.container.changeWin(GameWindow(self.container, self, self.question))

    """ A chaque tour..."""
    def next_turn(self, reponse, question):
        if question.verifReponse(reponse):
            self.answers.append(True)
        question.destroy()
        self.question = self.listQuestion[self.tour]
        print(self.listQuestion[self.tour].reponseList[1])
        if self.tour < self.SIZE_PARTIE - 1:
            self.tour += 1
            self.container.changeWin(GameWindow(self.container, self, self.question))
        else:
            self.container.changeWin(EndWindow(self.container, self))


    """ Calcule le score à la fin de la partie, renvoie le pourcentage de
    réussite. """
    def calculate_score(self, tenBoolList):
        score = 0
        for i in (self.SIZE_PARTIE):
            if tenBoolList[i] is True:
                score = score + 10
        return score
