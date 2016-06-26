import os, sys
from tkinter import *
from ConnWindow import *

class Interface:
    """
        L'interface graphique d'une partie de quizz.
    """

    largeur = 800
    hauteur = 500

    canvas = None
    root = None

    frameLog = None

    partie = None

    def __init__(self):
        self.root = Tk()
        self.root.title = "Quizz"
        self.root.geometry(str(self.largeur)+"x"+str(self.hauteur)+"+500+300")
        self.canvas = Canvas(self.root,
                                bg="white",
                                width=self.largeur,
                                height=self.hauteur)
        self.canvas.pack()
        self.changeWin(ConnWindow(self))


    def changeWin(self, window):
        print ("Refresh")
        self.frameLog = window
        self.frameLog.interface = self
        self.root.mainloop()
