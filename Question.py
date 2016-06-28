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
		print(row[3])
		self.idQuest = row[0]
		self.text = row[1]
		self.bonneReponse = row[2]
		i = 0
		for i in range(3, len(row)):
			print("Rang:" + str(i) + ". Reponse:" + row[i])
			self.reponseList.append(row[i])




	def verifReponse(self, reponse):
		if(reponse == self.bonneReponse):
			print("Bonne reponse")
			return True

		else:
			print ("Mauvaise Réponse")
			return False
