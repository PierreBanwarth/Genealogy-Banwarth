from meza import io

from xml.dom import minidom
import xml.etree.ElementTree as ET
from tkinter import *


tree = ET.parse('data/table1.xml')
root = tree.getroot()
# all item attributes



def recupererParSosa(sosa, root):
    resultatRecherche = None
    for element in root:
        for sousElement in element:
            if sousElement != None and sousElement.tag == 'Sosa' and sousElement.text == str(sosa):
                resultatRecherche = element

    return resultatRecherche


def afficherEnConsoleElement(element):
    for sousElement in element:
        print(str(sousElement.tag)+' : '+ str(sousElement.text))

def Agnatique(sosa):
    print('on recherche le sosa :' + str(sosa))

    resultatRecherche = recupererParSosa(sosa, root)
    afficherEnConsoleElement(resultatRecherche)
    print('===========================================================================')
    while resultatRecherche != None:
        sosa = sosa + sosa
        print('on recherche le sosa :' + str(sosa))
        resultatRecherche = recupererParSosa(sosa, root)
        if resultatRecherche != None:
            afficherEnConsoleElement(resultatRecherche)
        else:
            print('fin de la branche')
        print('===========================================================================')




Agnatique(2)











#     liste.insert(i, item)
def affichage():
    fenetre = Tk()
    fenetre['bg']='white'

    # https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
    # Haut
    Haut = Frame(fenetre)
    Haut.pack(side=TOP,fill=BOTH,expand=1)

    # Personnage et photo
    Millieu = Frame(fenetre)
    Millieu.pack(side=TOP, fill=BOTH,expand=1)

    Bas = Frame(fenetre, bg="white")
    Bas.pack(side=TOP, fill=BOTH,expand=1)


    # Frame du pere
    Pere = LabelFrame(Haut, text='pere', borderwidth=2, relief=GROOVE)
    Pere.pack(side=LEFT, fill=BOTH,expand=1)

    #Frame de la mere
    Mere = LabelFrame(Haut, text='mere', borderwidth=2, relief=GROOVE)
    Mere.pack(side=LEFT, fill=BOTH,expand=1)

    Photo = LabelFrame(Millieu, text='photo', borderwidth=2, relief=GROOVE)
    Photo.pack(side=LEFT)

    Personnage = LabelFrame(Millieu,  text='Personne', borderwidth=2, relief=GROOVE)
    Personnage.pack(side=LEFT, fill=BOTH,expand=1)

    # frame 3 dans frame 2


    Mariage = LabelFrame(Bas, text='Mariage(s)', borderwidth=2, relief=GROOVE)
    Mariage.pack(side=LEFT, fill=BOTH,expand=1)


    Enfant = LabelFrame(Bas, text='Enfant(s)', borderwidth=2, relief=GROOVE)
    Enfant.pack(side=LEFT, fill=BOTH,expand=1)


    Fratrie = LabelFrame(Bas, text='Fratrie', borderwidth=2, relief=GROOVE)
    Fratrie.pack(side=LEFT, fill=BOTH,expand=1)



    # Ajout de labels
    Label(Mere, text="Mere").pack(padx=10, pady=10)
    Label(Pere, text="Pere").pack(padx=10, pady=10)

    Label(Photo, text="Photo").pack(padx=10, pady=10)
    Label(Personnage, text="Personnage").pack(padx=10, pady=10)

    Label(Mariage, text="Mariage").pack(padx=10, pady=10)
    Label(Enfant, text="Enfant").pack(padx=10, pady=10)
    Label(Fratrie, text="Fratrie").pack(padx=10, pady=10)


    fenetre.mainloop()
