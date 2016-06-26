import os, sys
from random import randint
from Connector import *
from Question import *

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

    """ Déroulement de la partie. """
    def whole_game(self):
        answers = []
        for i in range(self.SIZE_PARTIE):
            answers[i] = self.ask_question(listQuestion[i])
        self.scorePartie = self.calculate_score(answers)

    """ Pose une question, renvoie un booléen en fonction de la validité de la
    réponse. """
    #def ask_question(self, question):

    """ Calcule le score à la fin de la partie, renvoie le pourcentage de
    réussite. """
    def calculate_score(self, tenBoolList):
        score = 0
        for i in (self.SIZE_PARTIE):
            if tenBoolList[i] is True:
                score = score + 10
        return score
