import json
from xml.dom import minidom
import xml.etree.ElementTree as ET
from tkinter import *
from person import *
from personneLabel import PersonneLabel
from functools import partial


try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def trouveDate(s):
    return any(i.isdigit() for i in s)

def formatDate(s):
    #"DateNaissance": "1833-05-21T00:00:00",
    if len(s) == len('1833-05-21T00:00:00'):
        array = s.split('T')[0].split('-')
        return array[2]+'/'+array[1]+'/'+array[0]
    else:
        print(s)

def dateEnfantFormat(s):
    array = s.split('/')
    result = ''
    if len(array) == 3:
        if len(array[0]) == 1:
            array[0] = '0'+array[0]
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

def convertirBase(racine):
    listPersonne = {}
    lieux = []

    nombreEnfants = 0
    nombreEnfantsUnknown = 0
    nombreConjoints = 0
    nombreConjointsUnknown = 0

    for element in racine:
        personne = {}
        conjoints = []

        enregistrement = False
        for sousElement in element:
            if sousElement != None and sousElement.text != None and sousElement.tag != None:

                if sousElement.tag == 'Br':
                    personne['Branche'] = sousElement.text

                elif sousElement.tag.startswith('Lieu'):
                    # JSON file
                    f = open ('data/departements-region.json', "r")
                    # Reading from file
                    data = json.loads(f.read())
                    lieu = getLieuxFromString(sousElement.text)
                    if 'departement' in lieu:
                        for item in data:
                            if str(item['num_dep']) == str(lieu['departement']):
                                lieu['departementName'] = item['dep_name']
                                lieu['regionName'] = item['region_name']

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
                    enregistrement = True
                    personne['Enregistrement'] = sousElement.text
                elif sousElement.tag == 'Rel':
                    personne['Religion'] = sousElement.text
                elif sousElement.tag == 'Profession':
                    if sousElement.text[0] == '-' or sousElement.text[0] == '+':
                        personne['Profession'] = sousElement.text[1:]
                elif sousElement.tag == 'Conj' or sousElement.tag == 'Conjoint2':
                    conjoint = {}
                    nombreConjoints = nombreConjoints + 1
                    infosConjoint = sousElement.text.split(' ')
                    while '' in  infosConjoint:
                        infosConjoint.remove('')
                    for s in infosConjoint:
                        if trouveDate(s):
                            conjoint['dateMariage'] = s
                            #infosConjoint.remove(s)

                    if len(infosConjoint) == 2:
                        conjoint['Nom'] = infosConjoint[0]
                        conjoint['prenom'] = infosConjoint[1]
                    elif len(infosConjoint) == 3 and not trouveDate(infosConjoint[2]):
                        if infosConjoint[1].isupper():
                            conjoint['Nom'] = infosConjoint[0] +' '+ infosConjoint[1]
                            conjoint['prenom'] = infosConjoint[2]
                        else:
                            conjoint['Nom'] = infosConjoint[0]
                            conjoint['prenom'] = infosConjoint[1] +' '+ infosConjoint[2]

                    elif len(infosConjoint) > 3:
                        # print(infosConjoint)
                        nombreConjointsUnknown = nombreConjointsUnknown + 1
                        conjoint['info'] = sousElement.text

                    conjoints.append(conjoint)
                elif sousElement.tag == 'Enfants':
                    text = sousElement.text
                    listeEnfants = text.split('\n')
                    ListeEnfantFinale = []
                    for enfant in listeEnfants:
                        nombreEnfants = nombreEnfants+1
                        infosEnfant = enfant.split(' ')
                        # on regarde les dates approximatives
                        # x + et o
                        # x mariage

                        # + deces
                        # o naissance
                        newEnfant = {}

                        if '+' in infosEnfant:
                            indexDeces = infosEnfant.index('+')+1
                            if indexDeces < len(infosEnfant):
                                newEnfant['dateDeces'] = infosEnfant[indexDeces]

                        if 'x' in infosEnfant:
                            indexMariage = infosEnfant.index('x')+1
                            if indexDeces < len(infosEnfant):
                                newEnfant['dateMariage'] = infosEnfant[indexMariage]

                        if '' in  infosEnfant:
                            infosEnfant.remove('')
                        elif 'vers' in infosEnfant or 'Vers' in infosEnfant:
                            if 'vers' in infosEnfant:
                                index = infosEnfant.index('vers')
                            elif 'Vers' in infosEnfant:
                                index = infosEnfant.index('Vers')

                            dateApprox = infosEnfant[index+1]

                            if len(infosEnfant) == 3:
                                newEnfant['nom1'] = infosEnfant[0]
                            if len(infosEnfant) == 4:
                                newEnfant['nom1'] = infosEnfant[0]
                                newEnfant['nom2'] = infosEnfant[1]
                            newEnfant['dateApprox'] = dateApprox

                        elif 'o' in infosEnfant:
                            indexO = infosEnfant.index('o')
                            indexNaissance = indexO+1
                            newEnfant['dateNaissance'] = dateEnfantFormat(infosEnfant[indexNaissance])
                            if indexO == 1:
                                newEnfant['nom1'] = infosEnfant[0]
                            elif indexO == 2:
                                newEnfant['nom1'] = infosEnfant[0]
                                newEnfant['nom2'] = infosEnfant[1]

                        elif len(infosEnfant) == 3 and '/' in infosEnfant[2]:
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['nom2'] = infosEnfant[1]
                            newEnfant['dateNaissance'] = dateEnfantFormat(infosEnfant[2])

                            #print('prenom : '+infosEnfant[0]+' nom : '+infosEnfant[1])
                            #print('date : '+infosEnfant[2])
                        elif len(infosEnfant) == 2 and '/' in infosEnfant[1]:
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['dateNaissance'] = dateEnfantFormat(infosEnfant[1])
                        elif infosEnfant[0] == '*':
                            pass
                        elif len(infosEnfant) == 1:
                            newEnfant['nom1'] = infosEnfant[0]
                        elif len(infosEnfant) == 3 and infosEnfant[1] == 'en':
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['dateNaissance'] = dateEnfantFormat(infosEnfant[2])
                        elif 'env' in infosEnfant or 'env.' in infosEnfant:
                            #cas nom prenom
                            if len(infosEnfant) == 3:
                                newEnfant['nom1'] = infosEnfant[0]
                                newEnfant['dateNaissance'] = dateEnfantFormat(infosEnfant[2])
                            if len(infosEnfant) == 4:
                                # 1= nom, 2 = env, 3 = date
                                newEnfant['nom1'] = infosEnfant[0]
                                newEnfant['nom2'] = infosEnfant[1]
                                newEnfant['dateNaissance'] = dateEnfantFormat(infosEnfant[3])

                            #cas nom
                        elif len(infosEnfant) >= 2 and trouveDate(infosEnfant[1]):
                            date = infosEnfant[1]
                            date = date.replace(',','/')
                            date = date.replace('.','/')
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['dateNaissance'] = dateEnfantFormat(date)

                        elif len(infosEnfant) >= 3 and trouveDate(infosEnfant[2]):
                            date = infosEnfant[2]
                            date = date.replace(',','/')
                            date = date.replace('.','/')
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['nom2'] = infosEnfant[1]
                            newEnfant['dateNaissance'] = dateEnfantFormat(date)
                        elif len(infosEnfant) == 2:
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['nom2'] = infosEnfant[1]

                        else:
                            nombreEnfantsUnknown = nombreEnfantsUnknown+1
                            #print(infosEnfant)
                        if newEnfant != {}:
                            ListeEnfantFinale.append(newEnfant)


                    ListeEnfantFinale.insert(0,{'Sosa' : 'ToFind'})
                    personne['enfants'] = ListeEnfantFinale
                else:
                    personne[sousElement.tag] = sousElement.text
        personne['conjoints'] = conjoints

        if enregistrement:
            enregistrement = personne['Enregistrement']
            del(personne['Enregistrement'])
            listPersonne[enregistrement] = personne


    sauvegardeBase(lieux, 'lieux.json')
    print('==== Enfants ====')
    print('''nombre d'enfants : '''+str(nombreEnfants))
    percentage = (100*nombreEnfantsUnknown)/nombreEnfants
    print('=> Pourcentage erreure enfant: '+str(percentage))

    print('==== Conjoints ====')
    print('nombre de conjoints : '+str(nombreConjoints))
    percentage = (100*nombreConjointsUnknown)/nombreConjoints
    print('=> Pourcentage erreure conjoints: '+str(percentage))

    return listPersonne

def retrouverEnfant(jsonBySosa):
    result = {}
    for key, val in jsonBySosa.items():
        personne = Person(val)

        sosaFils = str(personne.getSonSosa())
        fils = Person(jsonBySosa[sosaFils])

        if personne.isToFindSon():
            personne.addAine(fils)

        result[key] = personne.toJson()
    return result


def baseBySosa(json):
    test = {}
    for key, val in json.items():
        test[val['Sosa']] = val
#     liste.insert(i, item)
    return test

def affichage(jsonArbre, jsonPersonne):
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

    personneLabel = PersonneLabel(Person(jsonArbre["2"]), Personnage)

    def getFather(jsonPersonne, jsonArbre):
        pere = jsonArbre[str(jsonPersonne['Sosa']*2)]
        resultat = pere
        personneLabel.set(Person(resultat))

        buttonFather.configure(command=partial(getFather, resultat, jsonArbre))
        buttonMother.configure(command=partial(getMother, resultat, jsonArbre))
        buttonFils.configure(command=partial(getHeritier, resultat, jsonArbre))

    def getMother(jsonPersonne, jsonArbre):
        mere = jsonArbre[str(jsonPersonne['Sosa']*2+1)]
        resultat = mere
        personneLabel.set(Person(resultat))

        buttonMother.configure(command=partial(getMother, resultat, jsonArbre))
        buttonFather.configure(command=partial(getFather, resultat, jsonArbre))
        buttonFils.configure(command=partial(getHeritier, resultat, jsonArbre))

    def getHeritier(jsonPersonne, jsonArbre):
        if jsonPersonne['Sosa'] % 2 == 0:
            heritier = jsonArbre[str(int(jsonPersonne['Sosa']/2))]
        else:
            heritier = jsonArbre[str(int(jsonPersonne['Sosa']/2-1))]
        resultat = heritier
        personneLabel.set(Person(resultat))

        buttonFather.configure(command=partial(getFather, resultat, jsonArbre))
        buttonMother.configure(command=partial(getMother, resultat, jsonArbre))
        buttonFils.configure(command=partial(getHeritier, resultat, jsonArbre))

    buttonMother = Button(
        Mere,
        text="Mere",
        command=partial(getMother, jsonPersonne, jsonArbre)
    )

    buttonFather = Button(
        Pere,
        text="Pere",
        command=partial(getFather, jsonPersonne, jsonArbre)
    )
    buttonFils= Button(
        Millieu,
        text="Fils",
        command=partial(getHeritier, jsonPersonne, jsonArbre)
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



def sauvegardeBase(jsonFinal, filename):
    with open(filename, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(
            jsonFinal,
            indent=4, sort_keys=True,
            separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))
def openBase(filename):
    with open(filename) as json_file:
        return json.load(json_file)

def main():
    # arbre = ET.parse('data/table1.xml')
    # racine = arbre.getroot()
    #
    # jsonFinal = convertirBase(racine)
    # #On crée la base de donnée par sosa pour faciliter les recherches
    # jsonBySosa = baseBySosa(jsonFinal)
    # result = retrouverEnfant(jsonBySosa)
    #
    # sauvegardeBase(result,  'baseDeDonneeBySosa.json')
    result = openBase('baseDeDonneeBySosa.json')
    affichage(result, result['2'])
    # for key, val in jsonFinal.items():
    #     print(val['Sosa'])

if __name__ == "__main__":
    main()
