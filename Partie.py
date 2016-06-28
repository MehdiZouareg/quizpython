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

    #Le thème de la partie
    theme = None
    #La liste des questions posés
    listQuestion = []
    #Le joueur de la partie
    joueur = None
    #Le score de la partie
    scorePartie = None

    answers = []

    tour = 0

    """ CONSTRUCTOR """
    def __init__(self, theme, joueur):
        self.joueur = joueur
        self.theme = theme
        questions = Connector.get_questions_db(theme)
        size = len(questions) - 1
        print(size)
        for i in range(self.SIZE_PARTIE):
            rand = randint(0, size)
            nextQuest = Question(questions[rand])
            self.listQuestion.append(nextQuest)

    """ Début de la partie. """
    def new_game(self, container):
        self.tour = 0
        self.question = self.listQuestion[self.tour]
        self.container = container
        self.container.changeWin(GameWindow(self.container, self.joueur, self.theme, self, self.question))

    """ A chaque tour..."""
    def next_turn(self, reponse, question):
        if question.verifReponse(reponse):
            self.answers.append("Bonne réponse !")
        self.tour += 1
        if self.tour <= self.SIZE_PARTIE:
            self.container.changeWin(GameWindow(self.container, self.joueur, self.theme, self, self.listQuestion[self.tour]))
        else:
            self.container.changeWin(EndWindow(self.container, self.joueur, self.theme, self))


    """ Calcule le score à la fin de la partie, renvoie le pourcentage de
    réussite. """
    def calculate_score(self, tenBoolList):
        score = 0
        for i in (self.SIZE_PARTIE):
            if tenBoolList[i] is True:
                score = score + 10
        return score
