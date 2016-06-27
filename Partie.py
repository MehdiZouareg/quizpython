import os, sys
from random import randint
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
        size = len(questions)
        for i in range(self.SIZE_PARTIE):
            fig = randint(0, size)
            nextQuest = Question(questions[fig])
            listQuestion.append(nextQuest)

    """ Début de la partie. """
    def new_game(self, container):
        self.tour = 1
        self.container = container
        changeWin(GameWindow(self.container, self.joueur, self.theme, self))

    """ A chaque tour..."""
    def next_turn(self, reponse, question):
        if question.verifReponse(number):
            answers.append("Bonne réponse !")
        self.tour += 1
        if self.tour =< SIZE_PARTIE:
            changeWin(GameWindow(self.container, self.joueur, self.theme, self))
        else:
            changeWin(EndWindow(self.container, self.joueur, self.theme, self))


    """ Calcule le score à la fin de la partie, renvoie le pourcentage de
    réussite. """
    def calculate_score(self, tenBoolList):
        score = 0
        for i in (self.SIZE_PARTIE):
            if tenBoolList[i] is True:
                score = score + 10
        return score
