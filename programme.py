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
from classes.statistiques import *
import collections
from functools import partial
import graphviz

import os
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

PADDING=10

def affichage(treeExplorer, theme):

    fenetre = ttk.Window(themename=theme)

    # https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
    # Haut*
    mainFrame = ttk.Frame(fenetre)
    mainFrame.pack(padx=PADDING, pady=PADDING, fill=BOTH,expand=1)

    # Section Recherche par Sosa



    Bas = ttk.Labelframe(mainFrame, text='Statistiques',bootstyle="info")
    Bas.pack(padx=(0,PADDING), pady=(0,PADDING), side=BOTTOM,fill=BOTH,expand=1)

    Stat = StatistiquesLabel(Bas, treeExplorer)
    Stat.pack()


    Gauche = ttk.Frame(mainFrame)
    Gauche.pack(side=LEFT,fill=BOTH,expand=1, padx=(0,PADDING), pady=(0,PADDING))

    Droite = ttk.Labelframe(mainFrame, text='Arbre',bootstyle="primary")
    Droite.pack(side=RIGHT,fill=BOTH,expand=1, padx=(0,PADDING), pady=(0,PADDING))


    Recherche = ttk.Labelframe(Gauche, text='Recherche',bootstyle="info")
    Recherche.pack(side=TOP,fill=BOTH,expand=1, padx=(0,PADDING), pady=(0,PADDING))

    Parents = ttk.Frame(Gauche)
    Parents.pack(side=TOP,fill=X,expand=1)

    frameBouton = ttk.Labelframe(Gauche, text='Navigation', bootstyle="primary")
    frameBouton.pack(side=TOP,fill=X,expand=1, padx=(0,PADDING), pady=(0,PADDING))

    # Personnage et photo
    Millieu = ttk.Frame(Gauche)
    Millieu.pack(side=TOP, fill=X,expand=1)

    Bas = ttk.Frame(Gauche)
    Bas.pack(side=TOP, fill=X,expand=1)


    # Frame du pere
    Pere = ttk.Labelframe(Parents, text='Pere', bootstyle="primary")
    Pere.pack(side=LEFT,padx=(0,PADDING),pady=(0,PADDING),fill=X,expand=1)

    #Frame de la mere
    Mere =  ttk.Labelframe(Parents, text='Mere', bootstyle="primary")
    Mere.pack(side=LEFT,padx=(0,PADDING),pady=(0,PADDING),fill=X,expand=1)


    Personnage = ttk.Labelframe(Millieu, text='Personne', bootstyle="primary")
    Personnage.pack(side=LEFT, fill=BOTH,expand=1, padx=(0,PADDING), pady=(0,PADDING))

    Mariage = ttk.Labelframe(Bas, text='Mariage', bootstyle="primary")
    Mariage.pack(side=LEFT,fill=BOTH,expand=1, padx=(0,PADDING))

    Enfant = ttk.Labelframe(Bas, text='Enfant', bootstyle="primary")
    Enfant.pack(side=LEFT, fill=BOTH,expand=1, padx=(0,PADDING))



    Fratrie = ttk.Labelframe(Bas, text='Fratrie', bootstyle="primary")
    Fratrie.pack(side=LEFT, fill=BOTH,expand=1, padx=(0,PADDING))

    tree = Tree(Droite, treeExplorer)
    personneLabel = PersonneLabel(Personnage, Enfant, Pere, Mere, Mariage, Fratrie, treeExplorer)
    personneLabel.set(treeExplorer)



    entreeText = ttk.Entry(Recherche)
    entreeText.pack(side=LEFT,fill=BOTH,expand=1, padx=PADDING, pady=PADDING)


    def getBySosa(treeExplorer):
        result = treeExplorer.goToSosa()
        if result:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)

            buttonRecherhe.configure(command=partial(getBySosa, treeExplorer))
            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))
            buttonConjoint.configure(command=partial(getConjoint, treeExplorer))

    def getFather(treeExplorer):
        pere = treeExplorer.goToPere()
        if pere:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)
            buttonRecherhe.configure(command=partial(getBySosa, treeExplorer))
            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))
            buttonConjoint.configure(command=partial(getConjoint, treeExplorer))

    def getConjoint(treeExplorer):
        conjoint = treeExplorer.goToConjoint()
        if conjoint:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)

            buttonRecherhe.configure(command=partial(getBySosa, treeExplorer))
            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))
            buttonConjoint.configure(command=partial(getConjoint, treeExplorer))

    def getMother(treeExplorer):
        mere = treeExplorer.goToMere()

        if mere:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)

            buttonRecherhe.configure(command=partial(getBySosa, treeExplorer))
            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))
            buttonConjoint.configure(command=partial(getConjoint, treeExplorer))

    def getHeritier(treeExplorer):
        heritier = treeExplorer.goToHeritier()
        if heritier:
            personneLabel.set(treeExplorer)
            tree.canvasTree(treeExplorer)

            buttonRecherhe.configure(command=partial(getBySosa, treeExplorer))
            buttonFather.configure(command=partial(getFather, treeExplorer))
            buttonMother.configure(command=partial(getMother, treeExplorer))
            buttonFils.configure(command=partial(getHeritier, treeExplorer))
            buttonConjoint.configure(command=partial(getConjoint, treeExplorer))

    buttonMother = ttk.Button(
        frameBouton,
        text="Mere",

        command=partial(getMother, treeExplorer),
        bootstyle="primary"
    )

    buttonFather = ttk.Button(
        frameBouton,
        text="Pere",
        command=partial(getFather, treeExplorer),
        bootstyle="primary"
    )
    buttonFils= ttk.Button(
        frameBouton,
        text="Enfant",
        command=partial(getHeritier, treeExplorer),
        bootstyle="primary"
    )

    buttonConjoint= ttk.Button(
        frameBouton,
        text="Conjoint",
        command=partial(getConjoint, treeExplorer),
        bootstyle="primary"
    )

    buttonRecherhe= ttk.Button(
        Recherche,
        text="Rechercher par sosa",
        command=partial(getConjoint, treeExplorer),
        bootstyle="primary"
    )

    # Ajout de labels
    buttonFather.pack(side=LEFT, padx=PADDING, pady=PADDING)
    buttonMother.pack(side=LEFT, padx=PADDING, pady=PADDING)
    buttonFils.pack(side=LEFT, padx=PADDING, pady=PADDING)
    buttonConjoint.pack(side=LEFT, padx=PADDING, pady=PADDING)
    buttonRecherhe.pack(side=LEFT, padx=PADDING, pady=PADDING)

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
    affichage(treeExplorer, 'solar')
    # affichage(treeExplorer, 'superhero')
    # affichage(treeExplorer, 'darkly')
    # affichage(treeExplorer, 'vapor')
    # affichage(treeExplorer, 'cosmo')
    # affichage(treeExplorer, 'flatly')
    # affichage(treeExplorer, 'journal')
    # affichage(treeExplorer, 'litera')
    # affichage(treeExplorer, 'lumen')
    # affichage(treeExplorer, 'minty')
    # affichage(treeExplorer, 'sandstone')
    # affichage(treeExplorer, 'united')
    # affichage(treeExplorer, 'yeti')
    # affichage(treeExplorer, 'morph')
    # affichage(treeExplorer, 'simplex')
    # affichage(treeExplorer, 'cerculean')


if __name__ == "__main__":
    print('bienvenue Edouard')
    print('bienvenue Edouard')

    main()
