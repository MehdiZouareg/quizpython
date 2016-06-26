import os, sys
import sqlite3

class Connector:
	"""
		Classe qui assemble toutes les méthodes statiques interagissant avec la
		base de données.
	"""

	""" Si elle n'existe pas, créé la table 'joueur'. """
	@staticmethod
	def create_joueur_table():
		conn = sqlite3.connect('bdd_quizz.db')
		cursor = conn.cursor()
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS joueur(
			pseudo varchar(60) PRIMARY KEY UNIQUE,
			pourcentreussite int
		)
		""")
		conn.commit()
		conn.close()

	""" Si elle n'existe pas, créé la table 'partie'. """
	@staticmethod
	def create_partie_table():
		conn = sqlite3.connect('bdd_quizz.db')
		cursor = conn.cursor()
		cursor.execute("""
		CREATE TABLE IF NOT EXISTS partie(
			idpartie integer PRIMARY KEY AUTOINCREMENT UNIQUE,
			percentscore int,
			pseudo varchar(60),
			nomtheme varchar(60),
			FOREIGN KEY(pseudo) REFERENCES joueur(pseudo),
			FOREIGN KEY(nomtheme) REFERENCES theme(nomtheme)
		)
		""")
		conn.commit()
		conn.close()

	""" Si elle n'existe pas, créé la table 'theme'. """
	@staticmethod
	def create_theme_table():
			conn = sqlite3.connect('bdd_quizz.db')
			cursor = conn.cursor()
			cursor.execute("""
			CREATE TABLE IF NOT EXISTS theme(
				nomtheme varchar(60) PRIMARY KEY UNIQUE
			)
			""")
			conn.commit()
			conn.close()

	""" Si elle n'existe pas, créé la table 'question'. """
	@staticmethod
	def create_question_table():
	    conn = sqlite3.connect('bdd_quizz.db')
	    cursor = conn.cursor()
	    cursor.execute("""
	    CREATE TABLE IF NOT EXISTS question(
			idquest integer PRIMARY KEY AUTOINCREMENT UNIQUE,
			textquest varchar(127) UNIQUE,
			bonnerepquest varchar(127),
			reponse1 varchar(127),
			reponse2 varchar(127),
			reponse3 varchar(127),
			nomtheme varchar(60),
			FOREIGN KEY(nomtheme) REFERENCES theme(nomtheme)
	    )
	    """)
	    conn.commit()
	    conn.close()

	""" Récupère les questions correspondant à un thème dans la base de
	données. """
	@staticmethod
	def get_questions_db(chosenTheme):
		conn = sqlite3.connect('bdd_quizz.db')
		cursor = conn.cursor()
		cursor.execute("""SELECT * FROM question WHERE nomtheme = ?""", (str(chosenTheme),))
		rows = cursor.fetchall()
		conn.close()
		return rows

	""" Récupère tous les thèmes référencés dans la base de données. """
	@staticmethod
	def get_themes_db():
		query = """SELECT * FROM theme"""
		conn = sqlite3.connect('bdd_quizz.db')
		cursor = conn.cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		conn.close()
		return rows
