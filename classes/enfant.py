import datetime # we will use this for date objects
import json
from  classes.dates import *
from  classes.utils import *
import random

def enfantFromString(enfantString):

    infosEnfant = cleanString(enfantString)
    enfant = Enfant()
    if 'ondoye' in infosEnfant:
        pass

    resultat = getInfosDecesMariage(infosEnfant, 'DateDeces', '+')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateDeces(resultat['resultat'])

    resultat = getInfosDecesMariage(infosEnfant, 'DateNaissance', 'o')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateNaissance(resultat['resultat'])

    resultat = getInfosDecesMariage(infosEnfant, 'DateMariage', 'x')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateMariage(resultat['resultat'])

    resultat = trouveDateKey(infosEnfant, enfant, 'DateNaissance')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateNaissance(resultat['resultat'])

    enfant.Prenom = ' '.join(infosEnfant)
    return enfant

def enfantFromJson(json):
    enfants = []
    if len(json)>0:
        for item in json:
            enfant = Enfant()
            for key, value in item.items():
                if 'Prenom' == key:
                    enfant.Prenom = value
                elif 'Sosa' == key:
                    enfant.Sosa = value
                elif 'DateNaissance' in key:
                    enfant.DateNaissance = Date({'key':'DateNaissance', 'value':value})
                elif 'DateMariage'in key:
                    enfant.DateMariage = Date({'key':'DateMariage', 'value':value})
                elif 'DateDeces'in key:
                    enfant.DateDeces = Date({'key':'DateDeces', 'value':value})
            enfants.append(enfant)

    return enfants



class Enfant:
    def __init__(self):
        self.Prenom = ''
        self.DateNaissance = None
        self.DateMariage = None
        self.DateDeces = None
        self.Sosa = None

    def setJson(self, personne):
        self.Sosa = personne.getSosa()
        self.Prenom = personne.getNom()+' '+personne.getPrenom()
        self.DateNaissance = personne.DateNaissance
        self.DateDeces = personne.DateDeces
        self.DateMariage = personne.DateMariage

    def setDateNaissance(self, json):
        self.DateNaissance = Date(json)
    def getDateNaissance(self):
        return self.DateNaissance
    def getAnneeNaissance(self):
        if self.DateNaissance != None:
            if self.DateNaissance.getAnnee() != None:

                return int(self.DateNaissance.getAnnee())
        return None
    def setDateDeces(self, json):
        self.DateDeces = Date(json)

    def setDateMariage(self, json):
        self.DateMariage = Date(json)

    def __str__(self):
        string = self.Prenom
        if self.DateNaissance !=None:
            string = string+' Naissance : '+str(self.DateNaissance)
        if self.DateDeces !=None:
            string = string+ ' Deces : '+str(self.DateDeces)
        if self.DateMariage !=None:
            string = string+' Mariage : '+str(self.DateMariage)
        return string

    def getDisplayStr(self):
        sexe = 'F'
        if self.Sosa != None:
            if self.Sosa%2==0:
                sexe = 'M'
            else:
                sexe = 'F'

        if self.DateNaissance == None and self.DateDeces == None:
            resultat = """%s\n(%s) """ % (self.Prenom)
        if self.DateNaissance != None and self.DateDeces == None:
            resultat = """%s\nDate Naissance = %s""" % (self.Prenom, self.DateNaissance)
        if self.DateNaissance == None and self.DateDeces != None:
            resultat = """%s\nDate Deces = %s""" % (self.Prenom , self.DateDeces)
        if self.DateNaissance != None and self.DateDeces != None:
            resultat = """%s\nDate Naissance = %s\nDate Deces = %s""" % (self.Prenom, self.DateNaissance, self.DateDeces)
        return resultat
        # Louis XIV (M, birthday=1638-09-05, deathday=1715-09-01)

    def toJSON(self):
        result = {
            'Prenom' : self.Prenom
        }
        if self.Sosa != None:
            result['Sosa'] = self.Sosa
        if self.DateNaissance != None:
            result['DateNaissance'] = str(self.DateNaissance)
        if self.DateDeces !=None:
            result['DateDeces'] = str(self.DateDeces)
        if self.DateMariage !=None:
            result['DateMariage'] = str(self.DateMariage)
        return result
