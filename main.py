import json
from xml.dom import minidom
import xml.etree.ElementTree as ET
from tkinter import *
from classes.personne import *

from classes.personneLabel import PersonneLabel
from functools import partial

from  classes.fichiers import *


def trouveNom(s):
    return s.isupper() and len(s)>2
def formatShortDate(s):
    jour = ''
    mois = ''
    tab = s.split('/')
    if len(tab) !=3:
        return s
    else:

        if len(tab[0]) == 1:
            jour = '0'+tab[0]
        elif len(tab[0]) == 0:
            jour = '??'
        else:
            jour = tab[0]
        if len(tab[1]) == 1:
            mois = '0'+tab[1]
        else:
            mois = tab[1]
        return jour+'/'+mois+'/'+tab[2]
def goodFormatDate(s):
    return len(s.split('/')) == 3  and len(s.split('/')[0]) == 2 and len(s.split('/')[1]) == 2 and len(s.split('/')[2]) == 4
def goodFormatDateApproximative(s):
    return len(s.split('/')) == 2  and len(s.split('/')[0]) == 4 and len(s.split('/')[1]) == 4
def trouveDate(s):
    return any(i.isdigit() for i in s)
def isYear(s):
    return all(i.isdigit() for i in s) and (s[0] == '1' or s[0] == '2')
def formatDate(s):
    #"DateNaissance": "1833-05-21T00:00:00",
    if len(s) == len('1833-05-21T00:00:00'):
        array = s.split('T')[0].split('-')
        return array[2]+'/'+array[1]+'/'+array[0]

def dateEnfantFormat(s):
    array = s.split('/')
    result = ''
    if len(array) == 3:
        if len(array[0]) == 1:
            array[0] = '0'+array[0]
        elif len(array[0]) == 0:
            array[0] = '??'
        if len(array[1]) == 1:
            array[1] = '0'+array[1]
        return array[0]+'/'+array[1]+'/'+array[2]
    else:
        return s
def getLieuxFromString(s):
    if '*' in s:
        s = s.split('*')
        return {
            'departement' : s[0],
            'ville' : s[1]
        }

    else:
        s = s[1:]
        s = s.split(')')
        if s[0] == 'I':
            pays  ='Italie'
        if s[0] == 'D' or s[0] == 'B':
            pays  ='Swisse'
        if s[0] == 'S':
            pays  ='Allemagne'
        return {
            'pays' : pays,
            'ville' : s[1]
        }

def getInfosDecesMariage(tableauString, objet, key, str):
    if str in tableauString:
        indexChar = tableauString.index(str)
        index = indexChar+1

        if index < len(tableauString):
            resultat = tableauString[index]
            resultat = formatShortDate(resultat)
            if resultat == 'avant':
                resultat = tableauString[index+1]
                resultat = formatShortDate(resultat)
            objet[key] = resultat
        if len(tableauString) > index:
            tableauString.pop(index)
        tableauString.remove(str)

    return {
        'tableauString' : tableauString,
        'objet' : objet
    }


def trouveDateKey(s, tableauString, objet, key):
    if trouveDate(s):
        dateClean = formatShortDate(s)

        if goodFormatDate(dateClean) or isYear(dateClean):
            if 'vers' in tableauString:
                objet[key+'Approximative'] = 'vers ' + dateClean
                tableauString.remove('vers')
            elif 'avant' in tableauString:
                objet[key+'Approximative'] = 'avant ' + dateClean
                tableauString.remove('avant')
            elif 'apres' in tableauString:
                objet[key+'Approximative'] = 'apres ' + dateClean
                tableauString.remove('apres')
            else:
                objet[key] = dateClean
        elif goodFormatDateApproximative(dateClean):
            objet[key+'Approx'] = dateClean.split('/')[0] +' ou '+dateClean.split('/')[1]
        else:
            if len(dateClean.split('/')) != 3:
                pass
        index = tableauString.index(s)
        tableauString.pop(index)

    return {
        'tableauString' : tableauString,
        'objet' : objet
    }

def parseEnfants(s):
    ListeEnfantFinale = []
    listeEnfants = s.split('\n')


    for enfantString in listeEnfants:
        enfant = {}

        infosEnfant = cleanString(enfantString)

        if 'o' in infosEnfant:
            infosEnfant.remove('o')
        if 'ondoye' in infosEnfant:
            pass

        result = getInfosDecesMariage(infosEnfant, enfant, 'dateDeces', '+')
        infosEnfant = result['tableauString']

        if 'dateDeces' in result['objet']:
            enfant['dateDeces'] = result['objet']['dateDeces']

        result = getInfosDecesMariage(infosEnfant, enfant, 'dateMariage', 'x')
        infosEnfant = result['tableauString']

        if 'dateMariage' in result['objet']:
            enfant['dateMariage'] = result['objet']['dateMariage']

        if '*' in infosEnfant:
            ListeEnfantFinale.insert(0,{'Sosa' : 'ToFind'})
            infosEnfant.remove('*')

        else:
            for item in infosEnfant:
                result = trouveDateKey(item, infosEnfant, enfant, 'dateNaissance')
                infosEnfant = result['tableauString']
                enfant = result['objet']
                if 'dateNaissance' in result['objet']:
                    enfant['dateNaissance'] = result['objet']['dateNaissance']
                if 'dateNaissanceApproximative' in result['objet']:
                    enfant['dateNaissanceApproximative'] = result['objet']['dateNaissanceApproximative']
        enfant['Prenom'] = ' '.join(infosEnfant)
        ListeEnfantFinale.append(enfant)
    return ListeEnfantFinale



def cleanString(s):
    result = s.split(' ')
    while '' in  result:
        result.remove('')

    for i in range(len(result)):
        onlyX = True
        if 'X' in result[i]:
            for x in result[i]:
                if x != 'X':
                    onlyX = False
        if onlyX:
            result[i] = result[i].lower()
    return result

def parseConjoint(s):
    conjoint = {}
    infosConjoint = cleanString(s)
    TrouveDate = False
    result = getInfosDecesMariage(infosConjoint, conjoint, 'dateDeces', '+')
    infosConjoint = result['tableauString']
    conjoint = result['objet']
    for item in infosConjoint:
        result = trouveDateKey(item, infosConjoint, conjoint, 'dateMariage')
        infosConjoint = result['tableauString']
        conjoint = result['objet']

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
        conjoint['NumeroMariage'] = 2
    elif 'xx' in infosConjoint:
        infosConjoint.remove('xx')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 3
    elif 'xxx' in infosConjoint:
        infosConjoint.remove('xxx')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 4

    #
    # elif 'xxx' in infosConjoint:
    #     infosConjoint.remove('xxx')
    #     conjoint['Prenom'] = ' '.join(infosConjoint)

    elif(len(infosConjoint)==2):
        conjoint['Prenom'] = ' '.join(infosConjoint)
    else:
        conjoint['info'] = ' '.join(infosConjoint)
    # if 'Prenom' in conjoint:
    #     print(conjoint['Prenom'])
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
                    personne['DateNaissance'] = formatDate(sousElement.text)
                elif sousElement.tag == 'DDeces':
                    personne['DateDeces'] = formatDate(sousElement.text)
                elif sousElement.tag == 'Enregist':
                    personne['Enregistrement'] = sousElement.text
                elif sousElement.tag == 'Rel':
                    personne['Religion'] = sousElement.text
                elif sousElement.tag == 'Profession':
                    if sousElement.text[0] == '-' or sousElement.text[0] == '+':
                        personne['Profession'] = sousElement.text[1:]
                elif sousElement.tag == 'Conj':
                    nombreConjoints = nombreConjoints + 1
                    conjoint = parseConjoint(sousElement.text)
                    conjoints.append(conjoint)
                elif sousElement.tag == 'Conjoint2':
                    nombreConjoints = nombreConjoints + 1
                    infosConjoint = sousElement.text.split('\n')
                    for item in infosConjoint:
                        nombreConjoints = nombreConjoints + 1
                        conjoint = parseConjoint(item)
                        conjoints.append(conjoint)
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
        fils = jsonBySosa[sosaFils]

        if personne.isToFindSon():
            personne.addAine(fils)

        result[sosa] = personne
    return result



def affichage(arbre, personne):
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

    personneLabel = PersonneLabel(arbre["2"], Personnage, Enfant)

    def getFather(personne, arbre):
        pere = arbre[str(personne.getPere())]
        personneLabel.set(pere)

        buttonFather.configure(command=partial(getFather, pere, arbre))
        buttonMother.configure(command=partial(getMother, pere, arbre))
        buttonFils.configure(command=partial(getHeritier, pere, arbre))

    def getMother(personne, arbre):
        mere = arbre[str(personne.getMere())]
        personneLabel.set(mere)

        buttonMother.configure(command=partial(getMother, mere, arbre))
        buttonFather.configure(command=partial(getFather, mere, arbre))
        buttonFils.configure(command=partial(getHeritier, mere, arbre))

    def getHeritier(personne, arbre):

        heritier = arbre[str(personne.getHeritier())]
        personneLabel.set(heritier)

        buttonFather.configure(command=partial(getFather, heritier, arbre))
        buttonMother.configure(command=partial(getMother, heritier, arbre))
        buttonFils.configure(command=partial(getHeritier, heritier, arbre))

    buttonMother = Button(
        Mere,
        text="Mere",
        command=partial(getMother, personne, arbre)
    )

    buttonFather = Button(
        Pere,
        text="Pere",
        command=partial(getFather, personne, arbre)
    )
    buttonFils= Button(
        Millieu,
        text="Fils",
        command=partial(getHeritier, personne, arbre)
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

    result = openBaseBySosa('data/baseDeDonneeBySosa.json')


if __name__ == "__main__":
    main()
