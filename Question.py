import os, sys

class Question:
	"""
		La classe qui représente une question posée.
	"""

	#L'id de la question en base de donnée.
	idQuest = None
	#L'énoncé
	text = None
	#La réponse à fournir
	bonneReponse = None
	#Les autres choix
	reponseList = []

	""" CONSTRUCTOR """
	def __init__(self, row):
		self.idQuest = row[0]
		self.text = row[1]
		self.bonneReponse = row[2]
		i = 0
		for i in range(len(row)):
			reponseList.append(row[3][i])
			i+=1

    """ Pose une question, renvoie un booléen en fonction de la validité de la
    réponse. """

	def verifReponse(self, reponse):
		if(reponse == self.bonneReponse):
			print("Bonne reponse")
			return true

		else:
			print ("Mauvaise Réponse")
			return false
