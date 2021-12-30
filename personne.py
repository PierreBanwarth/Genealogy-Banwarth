import datetime # we will use this for date objects
import json
from fichiers import *


UNKNOWN = 'Sans'
astrologie = getAstrologie()
regnes = getRegnes()

class Personne:

    def getRegnes(self):
        regnesPersonne = []
        if self.DateNaissance != UNKNOWN and self.DateDeces != UNKNOWN and len(self.DateNaissance.split('/')) == 3 and len(self.DateDeces.split('/')) == 3:
            D = self.DateDeces.split('/')[2]
            N = self.DateNaissance.split('/')[2]
            for regne in regnes:
                    Dr = regne['dateDebut']
                    Fr = regne['dateFin']
                    if int(Dr) >= int(D) and int(D)>=int(Fr):
                        regnesPersonne.append(regne)
                    if int(Dr) >= int(N) and int(D)>=int(Fr):
                        regnesPersonne.append(regne)
        return regnesPersonne

    def getSigneAstro(self):
        date = self.DateNaissance
        dateArray = date.split('/')
        jour = int(dateArray[0])
        mois = int(dateArray[1])
        finded= False
        for signe in astrologie:
            dateDebutSigne = signe['dateDebut']
            dateFinSigne = signe['dateFin']
            jourDebutSigne = int(dateDebutSigne.split('/')[0])
            moisDebutSigne = int(dateDebutSigne.split('/')[1])

            jourFinSigne = int(dateFinSigne.split('/')[0])
            moisFinSigne = int(dateFinSigne.split('/')[1])
            if mois == moisDebutSigne:
                if jour >= jourDebutSigne:
                    finded = True
                    return signe['signe']
            if mois == moisFinSigne:
                if jour <= jourFinSigne:
                    finded = True
                    return signe['signe']
        if not finded:
            print(date)

    def __init__(self, json):

        self.Branche = json['Branche']
        if 'Aine' in json:
            self.Aine = json['Aine']
        else:
            self.Aine = UNKNOWN

        if 'Cadet' in json:
            self.Cadet = json['Cadet']
        else:
            self.Cadet = UNKNOWN

        if 'LieuDeces' in json:
            self.LieuDeces = json['LieuDeces']
        else:
            self.LieuDeces = UNKNOWN

        if 'MerePresentMariage' in json:
            self.MerePresentMariage = json['MerePresentMariage']
        else:
            self.MerePresentMariage = UNKNOWN

        if 'PerePresentMariage' in json:
            self.PerePresentMariage = json['PerePresentMariage']
        else:
            self.PerePresentMariage = UNKNOWN

        if 'Note' in json:
            self.Note = json['Note']
        else:
            self.Note = UNKNOWN

        if 'DateMariage' in json:
            self.DateMariage = json['DateMariage']
        else:
            self.DateMariage = UNKNOWN

        if 'DateDeces' in json:
            self.DateDeces = json['DateDeces']
        else:
            self.DateDeces = UNKNOWN

        if 'DateNaissance' in json:
            self.DateNaissance = json['DateNaissance']
        else:
            self.DateNaissance = UNKNOWN

        if 'LieuMariage' in json:
            self.LieuMariage = json['LieuMariage']
        else:
            self.LieuMariage = UNKNOWN

        if 'Religion' in json:
            self.Religion = json['Religion']
        else:
            self.Religion = UNKNOWN

        if 'Profession' in json:
            self.Profession = json['Profession']
        else:
            self.Profession = UNKNOWN

        if 'LieuNaissance' in json:
            self.LieuNaissance = json['LieuNaissance']
        else:
            self.LieuNaissance = UNKNOWN

        if 'Nom' in json:
            self.Nom = json['Nom']
        else:
            self.Nom = UNKNOWN
        if 'Prenom' in json:
            self.Prenom = json['Prenom']
        else:
            self.Nom = UNKNOWN

        self.Sosa = int(json['Sosa'])

        if (self.Sosa % 2) == 0:
            self.Male = True
        else:
            self.Male = False

        self.conjoints = json['conjoints']
        self.enfants = json['enfants']
        self.getRegnes()

    def getSonSosa(self):
        if self.Sosa <= 3:
            return self.Sosa
        if (self.Sosa % 2) == 0:
            return int(self.Sosa/2)
        else:
            return int((self.Sosa-1)/2)

    def isToFindSon(self):
        return 'Sosa' in self.enfants[0] and self.enfants[0]['Sosa']

    def addAine(self, personne):
        self.enfants.pop(0)
        self.enfants.insert(0,personne.getInfoHeritier())

    def getInfoHeritier(self):
        result = {}
        result['nom'] = self.Nom
        result['prenom'] = self.Prenom
        result['dateNaissance'] = self.DateNaissance
        return result

    def getPere(self):
        return self.Sosa*2

    def getMere(self):
        return (self.Sosa*2)+1
# "departement": "57",
# "departementName": "Moselle",
# "regionName": "Grand Est",
# "ville": "BAUDRECOURT"

    def getAge(self):
        return 'Todo calcul age'

    def getLieuNaissance(self):
        if self.LieuNaissance == UNKNOWN:
            return self.lieuNaissance
        else:
            lieux = getLieux()
            DictLieux = lieux[int(self.LieuNaissance)]
            if 'pays' in DictLieux:
                return DictLieux['pays']+' '+DictLieux['ville']
            else:
                return DictLieux['ville']+' '+ DictLieux['departementName']+'('+DictLieux['departement']+')'

    def getLieuDeces(self):
        if self.LieuDeces != UNKNOWN:
            with open('data/lieux.json') as json_file:
                lieux = json.load(json_file)
                DictLieux = lieux[int(self.LieuDeces)]
                if 'pays' in DictLieux:
                    return DictLieux['pays']+' '+DictLieux['ville']
                else:
                    return DictLieux['ville']+' '+ DictLieux['departementName']+'('+DictLieux['departement']+')'
        else:
            return self.LieuDeces

    def getLieuMariage(self):
        if self.LieuMariage != UNKNOWN:
            with open('data/lieux.json') as json_file:
                lieux = json.load(json_file)
                DictLieux = lieux[int(self.LieuMariage)]
                if 'pays' in DictLieux:
                    return DictLieux['pays']+' '+DictLieux['ville']
                else:
                    return DictLieux['ville']+' '+ DictLieux['departementName']+'('+DictLieux['departement']+')'
        else:
            self.lieuMariage

    def __str__(self):

        if self.Male:
            particule = 'Mr'
        else:
            particule = 'Mdme'
        return """
        =====================================
        Nom : %s %s %s
        Date de naissance : %s
        Sosa : %s
        =====================================
        """ % (particule, self.Nom, self.Prenom, self.DateNaissance, self.Sosa )

    def toJson(self):
        return {
            'Nom' : self.Nom,
            'Prenom' : self.Prenom,
            'DateNaissance' : self.DateNaissance,
            'Aine' : self.Aine,
            'Branche' : self.Branche,
            'Cadet' : self.Cadet,
            'DateMariage' : self.DateMariage,
            'DateDeces' : self.DateDeces,
            'LieuMariage' : self.LieuMariage,
            'LieuNaissance' : self.LieuNaissance,
            'Note' : self.Note,
            'PerePresentMariage' : self.PerePresentMariage,
            'MerePresentMariage' : self.MerePresentMariage,
            'Profession' : self.Profession,
            'Religion' : self.Religion,
            'Sosa' : self.Sosa,
            'conjoints' : self.conjoints,
            'enfants' : self.enfants,
        }
