import datetime # we will use this for date objects
import json
from  classes.dates import *
from  classes.utils import *

def enfantFromString(enfantString):

    infosEnfant = cleanString(enfantString)
    enfant = Enfant()
    if 'ondoye' in infosEnfant:
        pass

    resultat = getInfosDecesMariage(infosEnfant, 'dateDeces', '+')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateDeces(resultat['resultat'])

    resultat = getInfosDecesMariage(infosEnfant, 'dateNaissance', 'o')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateNaissance(resultat['resultat'])

    resultat = getInfosDecesMariage(infosEnfant, 'dateMariage', 'x')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateMariage(resultat['resultat'])

    resultat = trouveDateKey(infosEnfant, enfant, 'dateNaissance')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        enfant.setDateNaissance(resultat['resultat'])

    enfant.prenom = ' '.join(infosEnfant)
    return enfant
class Enfant:
    def __init__(self):
        self.prenom = ''
        self.dateNaissance = None
        self.dateMariage = None
        self.dateDeces = None

    def setJson(self, personne):

        self.prenom = personne.Prenom

        self.dateNaissance = Date({'key':'dateNaissance', 'value':personne.DateNaissance})
        self.dateDeces = Date({'key':'dateDeces', 'value':personne.DateDeces})
        self.dateMariage = Date({'key':'dateMariage', 'value':personne.DateMariage})

    def setDateNaissance(self, json):
        self.dateNaissance = Date(json)

    def setDateDeces(self, json):
        self.dateDeces = Date(json)

    def setDateMariage(self, json):
        self.dateMariage = Date(json)

    def __str__(self):
        string = self.prenom
        if self.dateNaissance !=None:
            string = string+' Naissance : '+str(self.dateNaissance)
        if self.dateDeces !=None:
            string = string+ ' Deces : '+str(self.dateDeces)
        if self.dateMariage !=None:
            string = string+' Mariage : '+str(self.dateMariage)
        return string

    def toJSON(self):
        result = {
            'Prenom' : self.prenom
        }
        if self.dateNaissance !=None:
            result['dateNaissance'] = str(self.dateNaissance)
        if self.dateDeces !=None:
            result['dateDeces'] = str(self.dateDeces)
        if self.dateMariage !=None:
            result['dateMariage'] = str(self.dateMariage)
        return result
