from meza import io

from xml.dom import minidom
import xml.etree.ElementTree as ET
from tkinter import *





def recupererParSosa(sosa, racine):
    resultatRecherche = None
    for element in racine:
        for sousElement in element:
            if sousElement != None and sousElement.tag == 'Sosa' and sousElement.text == str(sosa):
                resultatRecherche = element

    return resultatRecherche

def afficherEnConsoleElement(element):
    for sousElement in element:
        print(str(sousElement.tag)+' : '+ str(sousElement.text))

def definirPersonne(racine):
    listPersonne = []
    listlistEnfant = []
    nombreEnfants = 0
    unknown = 0
    for element in racine:
        personne = {}

        for sousElement in element:
            if sousElement != None and sousElement.text != None and sousElement.tag != None:
                personne[sousElement.tag] = sousElement.text

                if sousElement.tag == 'Enfants':
                    text = sousElement.text
                    listeEnfants = text.split('\n')

                    for enfant in listeEnfants:
                        nombreEnfants = nombreEnfants+1
                        infosEnfant = enfant.split(' ')
                        # on regarde les dates approximatives
                        # x + et o
                        # x mariage

                        # + deces
                        # o naissance

                        if '+' in infosEnfant:
                            indexDeces = infosEnfant.index('+')+1
                            if indexDeces < len(infosEnfant):
                                # print('Deces : '+infosEnfant[indexDeces])
                                pass
                        if 'x' in infosEnfant:
                            indexMariage = infosEnfant.index('x')+1
                            if indexDeces < len(infosEnfant):
                                # print('Mariage : '+infosEnfant[indexMariage])
                                pass
                        if '' in  infosEnfant:
                            infosEnfant.remove('')
                        elif 'vers' in infosEnfant:
                            index = infosEnfant.index('vers')
                            dateApprox = infosEnfant[index+1]
                        elif 'Vers' in infosEnfant:
                            index = infosEnfant.index('Vers')
                            dateApprox = infosEnfant[index+1]

                        elif 'o' in infosEnfant:
                            indexNaissance = infosEnfant.index('o')+1
                            pass
                        elif len(infosEnfant) == 3 and '/' in infosEnfant[2]:
                            pass
                            #print('prenom : '+infosEnfant[0]+' nom : '+infosEnfant[1])
                            #print('date : '+infosEnfant[2])
                        elif len(infosEnfant) == 2 and '/' in infosEnfant[1]:
                            pass
                            #print('prenom : '+infosEnfant[0])
                            #print('date : '+infosEnfant[1])
                        elif infosEnfant[0] == '*':
                            pass
                        elif len(infosEnfant) == 1:
                            #print('prenom : '+infosEnfant[0])
                            pass
                        elif len(infosEnfant) == 3 and infosEnfant[1] == 'en':
                            pass
                        elif len(infosEnfant) == 2 and len(infosEnfant[1]) == 4:
                            pass

                        else:
                            listlistEnfant.append(infosEnfant)
                            unknown = unknown+1
        listPersonne.append(personne)

    print('''nombre d'enfants : '''+str(nombreEnfants))
    percentage = (100*unknown)/nombreEnfants
    #nombre d'enfant = 100
    #unknown =
    print('Pourcentage : '+str(percentage))
    listlistEnfant.sort(key = len)
    for item in listlistEnfant:
        print(item)


def Agnatique(sosa):
    print('on recherche le sosa :' + str(sosaRecherche))

    resultatRecherche = recupererParSosa(sosaRecherche, racine)
    afficherEnConsoleElement(resultatRecherche)
    print('===========================================================================')
    while resultatRecherche != None:
        sosaRecherche = sosaRecherche + sosaRecherche
        print('on recherche le sosa :' + str(sosaRecherche))
        resultatRecherche = recupererParSosa(sosaRecherche, racine)
        if resultatRecherche != None:
            afficherEnConsoleElement(resultatRecherche)
        else:
            print('fin de la branche')
        print('===========================================================================')

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


def main():
    arbre = ET.parse('data/table1.xml')
    racine = arbre.getroot()
    definirPersonne(racine)
    # all item attributes
    # sosaRecherche = 2
    # Agnatique(2)


if __name__ == "__main__":
    main()
