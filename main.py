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
import collections
from functools import partial
import graphviz

import os
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'


lieux = []
def parseListeEnfants(s):
    listeEnfantFinale = []
    listeEnfants = s.split('\n')

    if '*' in listeEnfants:
        listeEnfants.remove('*')

    for enfantString in listeEnfants:
        enfant = enfantFromString(enfantString)
        listeEnfantFinale.append(enfant)
    return listeEnfantFinale




def parseConjoint(s):
    conjoint = {}
    infosConjoint = cleanString(s)
    TrouveDate = False
    resultat = getInfosDecesMariage(infosConjoint, 'dateDeces', '+')
    infosConjoint = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        conjoint['dateDeces'] = resultat['resultat']['value']

    resultat = getInfosDecesMariage(infosConjoint, 'dateNaissance', 'o')
    if resultat['resultat']['value'] != None:
        conjoint['dateNaissance'] = resultat['resultat']['value']

    resultat = trouveDateKey(infosConjoint, conjoint, 'DateMariage')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        conjoint['DateMariage'] = resultat['resultat']

    TrouveNom = False
    for item in infosConjoint:
        if(trouveNom(item)):
            if 'Nom' in conjoint:
                conjoint['Nom'] = conjoint['Nom']+' '+str(item)
            else:
                conjoint['Nom'] = str(item)
            infosConjoint.remove(item)
    # if 'Nom' in conjoint:
    #     print(conjoint['Nom'])
    if len(infosConjoint) == 1:
        conjoint['Prenom']  = ' '.join(infosConjoint)

    elif infosConjoint == ['xxx', 'xxxxx']:
        conjoint['Prenom'] = 'Inconnu'
        conjoint['Nom'] = 'Inconnu'
    elif 'x' in infosConjoint:
        infosConjoint.remove('x')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 1
    elif 'xx' in infosConjoint:
        infosConjoint.remove('xx')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 2
    elif 'xxx' in infosConjoint:
        infosConjoint.remove('xxx')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 3

    elif(len(infosConjoint)==2):
        conjoint['Prenom'] = ' '.join(infosConjoint)
    else:
        conjoint['info'] = ' '.join(infosConjoint)
    # if 'Prenom' in conjoint:
    #     print(conjoint['Prenom'])

    return conjoint



def convertirBase(racine):
    listPersonne = {}


    erreursEnfants = []
    erreursConjoints = []

    for element in racine:
        personne = Personne()
        conjoints = []

        for sousElement in element:
            if sousElement != None and sousElement.text != None and sousElement.tag != None:
                if sousElement.tag == 'Prenom':
                    personne.setPrenom(sousElement.text)
                elif sousElement.tag == 'PPM':
                    personne.setPerePresentMariage(sousElement.text)
                elif sousElement.tag == 'PMM':
                    personne.setMerePresenteMariage(sousElement.text)
                elif sousElement.tag == 'DMariage':
                    personne.setDateMariage(formatDate(sousElement.text))
                elif sousElement.tag == 'DNaissance':
                    personne.setDateNaissance(formatDate(sousElement.text))
                elif sousElement.tag == 'DDeces':
                    personne.setDateDeces(formatDate(sousElement.text))
                elif sousElement.tag == 'Enregist':
                    personne.setEnregistrement(sousElement.text)
                elif sousElement.tag == 'Rel':
                    personne.setReligion(sousElement.text)
                elif sousElement.tag == 'AdD':
                    personne.setAgeDeces(sousElement.text)
                elif sousElement.tag == 'RechEnf':
                    personne.setRechercheEnfantTermine()
                elif sousElement.tag == 'CdD':
                    personne.setConjointDecedesDeces(sousElement.text)
                elif sousElement.tag == 'Profession':
                    if sousElement.text[0] == '-' or sousElement.text[0] == '+':
                        personne.setProfession(sousElement.text[1:])
                elif sousElement.tag == 'Nom':
                    personne.setNom(sousElement.text)
                elif sousElement.tag == 'Br':
                    personne.setBranche(sousElement.text)
                elif sousElement.tag == 'Sosa':
                    personne.setSosa(sousElement.text)
                elif sousElement.tag == 'Cadet':
                    personne.setCadet(sousElement.text)
                elif sousElement.tag == 'Note':
                    personne.setNote(sousElement.text)
                elif sousElement.tag == 'Aine':
                    personne.setAine(sousElement.text)

                elif sousElement.tag == 'LieuNaissance':
                    personne.setLieuNaissance(sousElement.text)
                elif sousElement.tag == 'LieuDeces':
                    personne.setLieuDeces(sousElement.text)
                elif sousElement.tag == 'LieuMariage':
                    personne.setLieuMariage(sousElement.text)


                elif sousElement.tag == 'Conj':
                    conjoint = parseConjoint(sousElement.text)
                    conjoints.append(conjoint)
                elif sousElement.tag == 'Conjoint2':
                    infosConjoint = sousElement.text.split('\n')
                    for item in infosConjoint:
                        conjoint = parseConjoint(item)
                        conjoints.append(conjoint)
                elif sousElement.tag == 'Enfants':
                    personne.setEnfants(parseListeEnfants(sousElement.text))
                    # print(personne.getEnfants())

        personne.setConjoint(conjoints)
        sosa = personne.getSosa()
        listPersonne[int(sosa)] = personne

    return listPersonne

def retrouverEnfant(jsonBySosa):
    result = {}
    for sosa, personne in jsonBySosa.items():
        sosaFils = personne.getSonSosa()
        if sosa != sosaFils:
            fils = Enfant()
            fils.setJson(jsonBySosa[sosaFils])

            personne.addAine(fils)
        result[sosa] = personne
    return result

def affichage(arbre, personnePrincipale):
    fenetre = ttk.Window(themename="cosmo")

    # https://python.doctor/page-tkinter-interface-graphique-python-tutoriel
    # Haut*
    Gauche = ttk.Frame(fenetre)
    Gauche.pack(side=LEFT,fill=BOTH,expand=1)

    Droite = ttk.Labelframe(fenetre, text='Arbre',bootstyle="dark")
    Droite.pack(side=RIGHT,fill=BOTH,expand=1)



    Haut = ttk.Frame(Gauche)
    Haut.pack(side=TOP,fill=BOTH,expand=1)

    # Personnage et photo
    Millieu = ttk.Frame(Gauche)
    Millieu.pack(side=TOP, fill=BOTH,expand=1)

    Bas = ttk.Frame(Gauche)
    Bas.pack(side=TOP, fill=BOTH,expand=1)


    # Frame du pere
    Pere = ttk.Frame(Haut)
    Pere.pack(side=LEFT, fill=BOTH,expand=1)

    #Frame de la mere
    Mere = ttk.Frame(Haut)
    Mere.pack(side=LEFT, fill=BOTH,expand=1)

    Personnage = ttk.Frame(Millieu)
    Personnage.pack(side=LEFT, fill=BOTH,expand=1)


    tree = Tree(Droite, arbre)

    Mariage = ttk.Frame(Bas)
    Mariage.pack(side=LEFT, fill=BOTH,expand=1)


    Enfant = ttk.Frame(Bas)
    Enfant.pack(side=LEFT, fill=BOTH,expand=1)


    Fratrie = ttk.Frame(Bas)
    Fratrie.pack(side=LEFT, fill=BOTH,expand=1)

    personneLabel = PersonneLabel(personnePrincipale, Personnage, Enfant, Pere, Mere, arbre)



    def getFather(personnePrincipale, arbre):
        pere = arbre[personnePrincipale.getPere()]
        personneLabel.set(pere, Personnage, arbre)
        tree.canvasTree(arbre, personnePrincipale.getPere())

        buttonFather.configure(command=partial(getFather, pere, arbre))
        buttonMother.configure(command=partial(getMother, pere, arbre))
        buttonFils.configure(command=partial(getHeritier, pere, arbre))

    def getMother(personnePrincipale, arbre):
        mere = arbre[personnePrincipale.getMere()]
        personneLabel.set(mere, Personnage, arbre)
        tree.canvasTree(arbre, personnePrincipale.getMere())

        buttonMother.configure(command=partial(getMother, mere, arbre))
        buttonFather.configure(command=partial(getFather, mere, arbre))
        buttonFils.configure(command=partial(getHeritier, mere, arbre))

    def getHeritier(personnePrincipale, arbre):

        heritier = arbre[personnePrincipale.getHeritier()]
        personneLabel.set(heritier, Personnage, arbre)
        tree.canvasTree(arbre, personnePrincipale.getHeritier())

        buttonFather.configure(command=partial(getFather, heritier, arbre))
        buttonMother.configure(command=partial(getMother, heritier, arbre))
        buttonFils.configure(command=partial(getHeritier, heritier, arbre))

    buttonMother = ttk.Button(
        Mere,
        text="Mere",
        command=partial(getMother, personnePrincipale, arbre),
        bootstyle="primary"
    )

    buttonFather = ttk.Button(
        Pere,
        text="Pere",
        command=partial(getFather, personnePrincipale, arbre),
        bootstyle="primary"
    )
    buttonFils= ttk.Button(
        Millieu,
        text="Fils",
        command=partial(getHeritier, personnePrincipale, arbre),
        bootstyle="primary"
    )

    # Ajout de labels
    buttonFather.pack()
    buttonMother.pack()
    buttonFils.pack()

    personneLabel.pack()
    # frame 3 dans frame 2
    fenetre.mainloop()

def convertXMLFile():
    arbre = ET.parse('data/table1.xml')
    racine = arbre.getroot()
    jsonBySosa = convertirBase(racine)
    result = retrouverEnfant(jsonBySosa)
    sauvegardeBasePersonne(jsonBySosa, 'data/baseDeDonneeBySosa.json')

def plotRepartitionAnnuelle(result):
    test = {}
    for k, v in result.items():
        year = v.getAnneeNaissance()
        if year != None:
            if year not in test:
                test[int(year)] = 1
            else:
                test[int(year)] = test[year]+1
        for item in v.getEnfants():
            if item.getDateNaissance() != None:
                year = item.getAnneeNaissance()
                if year != None:
                    if year not in test:
                        test[year] = 1
                    else:
                        test[year] = test[year]+1
    od = collections.OrderedDict(sorted(test.items()))
    names = []
    values = []

    for k, v in test.items():
        names.append(k)
        values.append(v)


def main():
    # convertXMLFile()
    arbre = openBaseBySosa('data/baseDeDonneeBySosa.json')
    # plotRepartitionAnnuelle(result)
    # plotPngForThirdGen(arbre)
    # test(arbre, 2)
    affichage(arbre, arbre[2])


if __name__ == "__main__":
    main()
