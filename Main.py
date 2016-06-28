import os, sys
from Interface import *

def main():
    Connector.create_partie_table()
    Connector.create_theme_table()
    Connector.create_question_table()
    Connector.create_joueur_table()
    cadre = Interface()

if __name__ == '__main__':
    main()
