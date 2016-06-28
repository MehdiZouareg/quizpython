import os, sys

class Question:
	"""
		La classe qui représente une question posée.
	"""


	""" CONSTRUCTOR """
	def __init__(self, row):
		self.reponseList = []
		self.idQuest = row[0]
		self.text = row[1]
		self.bonneReponse = row[2]
		for i in range(3, 6):
			self.reponseList.append(row[i])
		self.reponseList.append(self.bonneReponse)
		print(self.reponseList)

	def verifReponse(self, reponse):
		if(reponse == self.bonneReponse):
			print("Bonne reponse")
			return True
		else:
			print ("Mauvaise Réponse")
			return False

	def destroy(self):
		self = None
