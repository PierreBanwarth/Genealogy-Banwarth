import json
from xml.dom import minidom
import xml.etree.ElementTree as ET

import pydot
import tkinter as tk

from numpy import arange, sin, pi
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from classes.personne import *
from classes.dates import *
from classes.enfant import *
from classes.personneLabel import PersonneLabel
from classes.utils import *
from classes.tree import *
from classes.fichiers import *
from classes.treeExplorer import *
import collections
from functools import partial
import graphviz

import os
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'



def affichage(treeExplorer):
    fenetre = ttk.Window(themename="cosmo")

    # https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
    # Haut*
    mainFrame = ttk.Frame(fenetre)
    mainFrame.pack(padx=10, pady=10)
    Gauche = ttk.Frame(mainFrame)
    Gauche.pack(side=LEFT,fill=BOTH,expand=1)

    Droite = ttk.Labelframe(mainFrame, text='Arbre',bootstyle="dark")
    Droite.pack(side=RIGHT,fill=BOTH,expand=1)



    Haut = ttk.Frame(Gauche)
    Haut.pack(side=TOP,fill=X,expand=1)

    # Personnage et photo
    Millieu = ttk.Frame(Gauche)
    Millieu.pack(side=TOP, fill=X,expand=1)

    Bas = ttk.Frame(Gauche)
    Bas.pack(side=TOP, fill=X,expand=1)


    # Frame du pere
    Pere = ttk.Labelframe(Haut, text='Pere', bootstyle="secondary")
    Pere.pack(side=LEFT,padx=(0,10))

    #Frame de la mere
    Mere =  ttk.Labelframe(Haut, text='Mere', bootstyle="secondary")
    Mere.pack(side=LEFT,padx=(0,10))


    Personnage = ttk.Labelframe(Millieu, text='Personne', bootstyle="primary")
    Personnage.pack(side=LEFT, fill=BOTH,expand=1,padx=(0,10))

    Mariage = ttk.Labelframe(Bas, text='Mariage', bootstyle="primary")
    Mariage.pack(side=LEFT,padx=(0,10))

    Enfant = ttk.Labelframe(Bas, text='Enfant', bootstyle="primary")
    Enfant.pack(side=LEFT, fill=BOTH,expand=1)


    Fratrie = ttk.Frame(Bas)
    Fratrie.pack(side=LEFT, fill=BOTH,expand=1)

    tree = Tree(Droite, treeExplorer)
    personneLabel = PersonneLabel(Personnage, Enfant, Pere, Mere, Mariage, treeExplorer)
    personneLabel.set(treeExplorer)

    def getFather(treeExplorer):
        pere = treeExplorer.goToPere()
        if pere:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)

            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))

    def getMother(treeExplorer):
        mere = treeExplorer.goToMere()

        if mere:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)

            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))

    def getHeritier(treeExplorer):
        heritier = treeExplorer.goToHeritier()
        if heritier:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)

            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))

    buttonMother = ttk.Button(
        Mere,
        text="Mere",
        command=partial(getMother, treeExplorer),
        bootstyle="primary"
    )

    buttonFather = ttk.Button(
        Pere,
        text="Pere",
        command=partial(getFather, treeExplorer),
        bootstyle="primary"
    )
    buttonFils= ttk.Button(
        Personnage,
        text="Enfant",
        command=partial(getHeritier, treeExplorer),
        bootstyle="primary"
    )

    # Ajout de labels
    buttonFather.pack(side=BOTTOM, padx=10, pady=10)
    buttonMother.pack(side=BOTTOM, padx=10, pady=10)
    buttonFils.pack(side=BOTTOM, padx=10, pady=10)

    personneLabel.pack()
    # frame 3 dans frame 2
    fenetre.mainloop()




def main():
    # convertXMLFile()
    arbre = openBaseBySosa('data/baseDeDonneeBySosa.json')
    # plotRepartitionAnnuelle(result)
    # plotPngForThirdGen(arbre)
    # test(arbre, 2)
    treeExplorer = TreeExplorer(2, arbre)
    # print(explorer.getCurrentPersonne())
    # print(explorer.getMere())
    # print(explorer.getPere())
    affichage(treeExplorer)


if __name__ == "__main__":
    main()
