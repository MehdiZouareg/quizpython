import os, sys

class Question1:
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
	def __init__(self):
		self.number = 1
		self.idQuest = 1
		self.text = "Lorsqu'un pancake prend l'avion à destination \nde Toronto et qu'il fait une escale technique \nà St-Claude, on dit :"
		self.bonneReponse = "La réponse D"
		self.reponseList = ["","","",""]
		self.reponseList[0] = "Qu'il n'est pas arrivé à Toronto"
		self.reponseList[1] = "Qu'il était supposé arriver à Toronto"
		self.reponseList[2] = "Qu'est-ce qu'il fout c'maudit \npancake tabernacle ?"
