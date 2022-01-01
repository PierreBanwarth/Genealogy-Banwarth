import json
from xml.dom import minidom
import xml.etree.ElementTree as ET
from tkinter import *

from classes.personne import *
from classes.dates import *
from classes.enfant import *
from classes.personneLabel import PersonneLabel
from classes.utils import *
from classes.fichiers import *

from functools import partial


def parseEnfants(s):
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
    result = getInfosDecesMariage(infosConjoint, conjoint, 'dateDeces', '+')
    infosConjoint = result['tableauString']
    conjoint = result['objet']

    result = getInfosDecesMariage(infosConjoint, conjoint, 'dateNaissance', 'o')

    infosConjoint = result['tableauString']
    conjoint = result['objet']

    result = trouveDateKey(infosConjoint, conjoint, 'dateMariage')
    infosConjoint = result['tableauString']
    if result['value'] != '':
        conjoint[result['key']] = result['value']

    TrouveNom = False
    for item in infosConjoint:
        if(trouveNom(item)):
            if 'Nom' in conjoint:
                conjoint['Nom'] = conjoint['Nom']+' '+str(item)
            else:
                conjoint['Nom'] = str(item)
            infosConjoint.remove(item)

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

    return conjoint

def convertirBase(racine):
    listPersonne = {}
    lieux = []

    erreursEnfants = []
    erreursConjoints = []

    nombreEnfants = 0
    nombreEnfantsUnknown = 0
    nombreConjoints = 0
    nombreConjointsUnknown = 0

    for element in racine:
        personne = {}
        conjoints = []

        Sosa = False
        for sousElement in element:
            if sousElement != None and sousElement.text != None and sousElement.tag != None:

                if sousElement.tag == 'Br':
                    personne['Branche'] = sousElement.text
                elif sousElement.tag == 'Sosa':
                    personne['Sosa'] = sousElement.text
                    Sosa = True
                elif sousElement.tag.startswith('Lieu'):
                    # JSON file
                    regions = getRegions()
                    lieu = getLieuxFromString(sousElement.text)
                    if 'departement' in lieu:
                        for region in regions:
                            if str(region['num_dep']) == str(lieu['departement']):
                                lieu['departementName'] = region['dep_name']
                                lieu['regionName'] = region['region_name']
                    if lieu not in lieux:
                        lieux.append(lieu)
                    index = lieux.index(lieu)
                    personne[sousElement.tag] = index

                elif sousElement.tag == 'PPM':
                    personne['PerePresentMariage'] = sousElement.text
                elif sousElement.tag == 'PMM':
                    personne['MerePresentMariage'] = sousElement.text
                elif sousElement.tag == 'DMariage':
                    personne['DateMariage'] = formatDate(sousElement.text)
                elif sousElement.tag == 'DNaissance':
                    personne['dateNaissance'] = formatDate(sousElement.text)
                elif sousElement.tag == 'DDeces':
                    personne['DateDeces'] = formatDate(sousElement.text)
                elif sousElement.tag == 'Enregist':
                    personne['Enregistrement'] = sousElement.text
                elif sousElement.tag == 'Rel':
                    personne['Religion'] = sousElement.text
                elif sousElement.tag == 'Profession':
                    if sousElement.text[0] == '-' or sousElement.text[0] == '+':
                        personne['Profession'] = sousElement.text[1:]
                # elif sousElement.tag == 'Conj':
                #     nombreConjoints = nombreConjoints + 1
                #     conjoint = parseConjoint(sousElement.text)
                #     conjoints.append(conjoint)
                # elif sousElement.tag == 'Conjoint2':
                #     nombreConjoints = nombreConjoints + 1
                #     infosConjoint = sousElement.text.split('\n')
                #     for item in infosConjoint:
                #         nombreConjoints = nombreConjoints + 1
                #         conjoint = parseConjoint(item)
                #         conjoints.append(conjoint)
                elif sousElement.tag == 'Enfants':
                    text = sousElement.text
                    personne['enfants'] = parseEnfants(text)

                else:
                    personne[sousElement.tag] = sousElement.text
        personne['conjoints'] = conjoints

        if Sosa:
            sosa = personne['Sosa']
            listPersonne[int(sosa)] = Personne(personne)


    sauvegardeBaseLieux(lieux)
    sauvegardeBase(erreursEnfants, 'erreursEnfants.json')
    sauvegardeBase(erreursConjoints, 'erreursConjoints.json')
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
    Mariage = LabelFrame(Bas, text='Mariage(s)', borderwidth=2, relief=GROOVE)
    Mariage.pack(side=LEFT, fill=BOTH,expand=1)


    Enfant = LabelFrame(Bas, text='Enfant(s)', borderwidth=2, relief=GROOVE)
    Enfant.pack(side=LEFT, fill=BOTH,expand=1)


    Fratrie = LabelFrame(Bas, text='Fratrie', borderwidth=2, relief=GROOVE)
    Fratrie.pack(side=LEFT, fill=BOTH,expand=1)

    personneLabel = PersonneLabel(personnePrincipale, Personnage, Enfant)

    def getFather(personnePrincipale, arbre):
        pere = arbre[personnePrincipale.getPere()]
        personneLabel.set(pere)

        buttonFather.configure(command=partial(getFather, pere, arbre))
        buttonMother.configure(command=partial(getMother, pere, arbre))
        buttonFils.configure(command=partial(getHeritier, pere, arbre))

    def getMother(personnePrincipale, arbre):
        mere = arbre[personnePrincipale.getMere()]
        personneLabel.set(mere)

        buttonMother.configure(command=partial(getMother, mere, arbre))
        buttonFather.configure(command=partial(getFather, mere, arbre))
        buttonFils.configure(command=partial(getHeritier, mere, arbre))

    def getHeritier(personnePrincipale, arbre):

        heritier = arbre[personnePrincipale.getHeritier()]
        personneLabel.set(heritier)

        buttonFather.configure(command=partial(getFather, heritier, arbre))
        buttonMother.configure(command=partial(getMother, heritier, arbre))
        buttonFils.configure(command=partial(getHeritier, heritier, arbre))

    buttonMother = Button(
        Mere,
        text="Mere",
        command=partial(getMother, personnePrincipale, arbre)
    )

    buttonFather = Button(
        Pere,
        text="Pere",
        command=partial(getFather, personnePrincipale, arbre)
    )
    buttonFils= Button(
        Millieu,
        text="Fils",
        command=partial(getHeritier, personnePrincipale, arbre)
    )

    # Ajout de labels
    Label(Mere, text="Mere").pack(padx=10, pady=10)
    Label(Pere, text="Pere").pack(padx=10, pady=10)

    Label(Photo, text="Photo").pack(padx=10, pady=10)
    Label(Personnage, text="Personnage").pack(padx=10, pady=10)

    Label(Mariage, text="Mariage").pack(padx=10, pady=10)
    Label(Enfant, text="Enfant").pack(padx=10, pady=10)
    Label(Fratrie, text="Fratrie").pack(padx=10, pady=10)
    buttonFather.pack()
    buttonMother.pack()
    buttonFils.pack()

    personneLabel.pack()

    # frame 3 dans frame 2


    fenetre.mainloop()



def main():
    arbre = ET.parse('data/table1.xml')
    racine = arbre.getroot()

    jsonBySosa = convertirBase(racine)
    result = retrouverEnfant(jsonBySosa)

    sauvegardeBasePersonne(result, 'data/baseDeDonneeBySosa.json')

    # result = openBaseBySosa('data/baseDeDonneeBySosa.json')
    # affichage(result, result[2])

if __name__ == "__main__":
    main()
