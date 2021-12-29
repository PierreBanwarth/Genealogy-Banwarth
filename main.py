from meza import io
import json
from xml.dom import minidom
import xml.etree.ElementTree as ET
from tkinter import *
from person import Person
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


def trouveDate(s):
    return any(i.isdigit() for i in s)

def convertirBase(racine):
    listPersonne = {}
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
                elif sousElement.tag == 'PPM':
                    personne['PerePresentMariage'] = sousElement.text
                elif sousElement.tag == 'PMM':
                    personne['MerePresentMariage'] = sousElement.text
                elif sousElement.tag == 'DMariage':
                    personne['DateMariage'] = sousElement.text
                elif sousElement.tag == 'DNaissance':
                    personne['DateNaissance'] = sousElement.text
                elif sousElement.tag == 'DDeces':
                    personne['DateDeces'] = sousElement.text
                elif sousElement.tag == 'Enregist':
                    enregistrement = True
                    personne['Enregistrement'] = sousElement.text
                elif sousElement.tag == 'Rel':
                    personne['Religion'] = sousElement.text
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
                            newEnfant['dateNaissance'] = infosEnfant[indexNaissance]
                            if indexO == 1:
                                newEnfant['nom1'] = infosEnfant[0]
                            elif indexO == 2:
                                newEnfant['nom1'] = infosEnfant[0]
                                newEnfant['nom2'] = infosEnfant[1]

                        elif len(infosEnfant) == 3 and '/' in infosEnfant[2]:
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['nom2'] = infosEnfant[1]
                            newEnfant['dateNaissance'] = infosEnfant[2]

                            #print('prenom : '+infosEnfant[0]+' nom : '+infosEnfant[1])
                            #print('date : '+infosEnfant[2])
                        elif len(infosEnfant) == 2 and '/' in infosEnfant[1]:
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['dateNaissance'] = infosEnfant[1]
                        elif infosEnfant[0] == '*':
                            pass
                        elif len(infosEnfant) == 1:
                            newEnfant['nom1'] = infosEnfant[0]
                        elif len(infosEnfant) == 3 and infosEnfant[1] == 'en':
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['dateNaissance'] = infosEnfant[2]
                        elif 'env' in infosEnfant or 'env.' in infosEnfant:
                            #cas nom prenom
                            if len(infosEnfant) == 3:
                                newEnfant['nom1'] = infosEnfant[0]
                                newEnfant['dateNaissance'] = infosEnfant[2]
                            if len(infosEnfant) == 4:
                                # 1= nom, 2 = env, 3 = date
                                newEnfant['nom1'] = infosEnfant[0]
                                newEnfant['nom2'] = infosEnfant[1]
                                newEnfant['dateNaissance'] = infosEnfant[3]

                            #cas nom
                        elif len(infosEnfant) >= 2 and trouveDate(infosEnfant[1]):
                            date = infosEnfant[1]
                            date = date.replace(',','/')
                            date = date.replace('.','/')
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['dateNaissance'] = date

                        elif len(infosEnfant) >= 3 and trouveDate(infosEnfant[2]):
                            date = infosEnfant[2]
                            date = date.replace(',','/')
                            date = date.replace('.','/')
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['nom2'] = infosEnfant[1]
                            newEnfant['dateNaissance'] = date
                        elif len(infosEnfant) == 2:
                            newEnfant['nom1'] = infosEnfant[0]
                            newEnfant['nom2'] = infosEnfant[1]

                        else:
                            nombreEnfantsUnknown = nombreEnfantsUnknown+1
                            #print(infosEnfant)
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
    # for item in listPersonne:
    #     print(item)
    print('==== Enfants ====')
    print('''nombre d'enfants : '''+str(nombreEnfants))
    percentage = (100*nombreEnfantsUnknown)/nombreEnfants
    print('     Pourcentage erreure enfant: '+str(percentage))

    print('==== Conjoints ====')
    print('nombre de conjoints : '+str(nombreConjoints))
    percentage = (100*nombreConjointsUnknown)/nombreConjoints
    print('     Pourcentage erreure conjoints: '+str(percentage))
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
        # if personne.Male:
        #     txtPersonne = 'Pere :'
        # else:
        #     txtPersonne = 'Mere :'
        # if fils.Male:
        #     txtHeritier = 'fils :'
        # else:
        #     txtHeritier = 'fille :'

        # print(txtPersonne+str(personne))
        # print(txtHeritier+str(fils))


def baseBySosa(json):
    test = {}
    for key, val in json.items():
        test[val['Sosa']] = val
#     liste.insert(i, item)
    return test

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

def sauvegardeBase(jsonFinal):
    with io.open('baseDeDonnee.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(
            jsonFinal,
            indent=4, sort_keys=True,
            separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

def main():
    arbre = ET.parse('data/table1.xml')
    racine = arbre.getroot()

    jsonFinal = convertirBase(racine)
    sauvegardeBase(jsonFinal)

    #On crée la base de donnée par sosa pour faciliter les recherches
    jsonBySosa = baseBySosa(jsonFinal)

    result = retrouverEnfant(jsonBySosa)
    sauvegardeBase(jsonFinal)

    # for key, val in jsonFinal.items():
    #     print(val['Sosa'])

if __name__ == "__main__":
    main()
