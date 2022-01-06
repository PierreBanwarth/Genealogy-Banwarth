import datetime # we will use this for date objects
import json
from  classes.fichiers import *
from classes.dates import *
from classes.enfant import *
from classes.lieux import *
astrologie = getAstrologie()
regnes = getRegnes()

def openBaseBySosa(filename):
    finalJson = {}
    json = openBase(filename)
    for sosa, json in json.items():
        personne = Personne()
        personne = personne.setPersonne(json)
        finalJson[int(sosa)] = personne
    return finalJson


class Personne:
    def __init__(self):
        self.Enfants = []
        self.Conjoints = []
        self.Branche = None
        self.Aine = None
        self.Cadet = None
        self.MerePresenteMariage = None
        self.PerePresentMariage = None
        self.Note = None
        self.DateMariage = None
        self.DateDeces = None
        self.DateNaissance = None
        self.LieuMariage = None
        self.LieuNaissance = None
        self.LieuDeces = None
        self.Sexe = None
        self.Profession = None
        self.Religion = None
        self.Nom = None
        self.Male = True
        self.Cadet = None
        self.Note = None
        self.Aine = None
        self.AgeDeces = None
        self.ConjointDecedesDeces = None
        self.RechercheEnfantTermine = False

    def getPrenom(self):
        return self.Prenom

    def getConjoints(self):
        return self.Conjoints

    def setConjoint(self, conjoints):
        self.Conjoints = conjoints

    def setConjointDecedesDeces(self, s):
        self.ConjointDecedesDeces = s

    def setRechercheEnfantTermine(self):
        self.setRechercheEnfantTermine = True

    def setPrenom(self, s):
        self.Prenom = s

    def setNom(self, s):
        self.Nom = s

    def getNom(self):
        return self.Nom

    def setBranche(self, s):
        self.Branche = s

    def setSexe(self):
        if self.Sosa % 2 == 0:
            self.Sexe = 'M'
        else:
            self.Sexe = 'F'

    def getSosa(self):
        return self.Sosa

    def setSosa(self, s):
        self.Sosa = int(s)
        self.setSexe()

    def setLieuDeces(self, s):
        self.LieuDeces = Lieu(s)

    def setLieuMariage(self, s):
        self.LieuMariage = Lieu(s)

    def setLieuNaissance(self, s):
        self.LieuNaissance = Lieu(s)

    def setPerePresentMariage(self, s):
        self.PerePresentMariage = s
    def setMerePresenteMariage(self, s):
        self.MerePresenteMariage = s

    def setDateMariage(self, s):
        self.DateMariage = Date({'key': 'DateMariage', 'value':s})
    def setDateNaissance(self, s):
        self.DateNaissance = Date({'key': 'DateNaissance', 'value':s})
    def setDateDeces(self, s):
        self.DateDeces = Date({'key': 'DateDeces', 'value':s})

    def setEnregistrement(self, s):
        self.Enregistrement = s
    def setReligion(self, s):
        self.Religion = s
    def setProfession(self, s):
        self.Profession = s
    def setEnfants(self, s):
        self.Enfants = s
    def setCadet(self, s):
        self.Cadet = s
    def setNote(self, s):
        self.Note = s
    def setAine(self, s):
        self.Aine = s
    def setAgeDeces(self, s):
        self.AgeDeces = s

    def getRegnes(self):
        regnesPersonne = []
        if self.DateNaissance != None and self.DateDeces != None and len(self.DateNaissance.split('/')) == 3 and len(self.DateDeces.split('/')) == 3:
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

    def getAnneeNaissance(self):
        if self.DateNaissance != None:
            return int(self.DateNaissance.getAnnee())
        else:
            return None

    def getEnfants(self):
        return self.Enfants

    def getSonSosa(self):
        if self.Sosa <= 3:
            return self.Sosa
        if self.Sosa % 2 == 0:
            return int(self.Sosa/2)
        else:
            return int((self.Sosa-1)/2)

    def isToFindSon(self):
        if len(self.Enfants)>0:
            return 'Sosa' in self.Enfants[0] and self.Enfants[0]['Sosa']

    def addAine(self, enfant):
        self.Enfants.insert(0,enfant)

    def getInfoHeritier(self):
        result = {}
        result['Prenom'] = self.Prenom
        result['dateNaissance'] = self.DateNaissance
        return result


    def getPere(self):
        return self.Sosa*2

    def getMere(self):
        return (self.Sosa*2)+1

    def getHeritier(self):
        if self.Sosa % 2 == 0:
            return int(self.Sosa/2)
        else:
            return int((self.Sosa-1)/2)

# "departement": "57",
# "departementName": "Moselle",
# "regionName": "Grand Est",
# "ville": "BAUDRECOURT"

    def getAge(self):
        return 'Todo calcul age'

    def getConjointSosa(self):
        if self.Sosa != None:
            if self.Sosa % 2 == 0:
                return self.Sosa+1
            else:
                return self.Sosa-1
        else:
            return 0
    def getBelleMaman(self):
        i = self.getConjointSosa()
        return (i*2)+1

    def getBeauPapa(self):
        i = self.getConjointSosa()
        return (i*2)

    def __str__(self):
        if self.Male:
            particule = 'Mr'
        else:
            particule = 'Mdme'
        return """%s %s""" % (self.Sosa, self.Nom)

    def getDisplayStr(self):
        if self.DateNaissance == None and self.DateDeces == None:
            resultat = """%s %s\nSosa : %s """ % (self.Nom, self.Prenom, self.Sosa)
        if self.DateNaissance != None and self.DateDeces == None:
            resultat = """%s %s\nSosa : %s\nN : %s """ % (self.Nom, self.Prenom, self.Sosa, self.DateNaissance)
        if self.DateNaissance == None and self.DateDeces != None:
            resultat = """%s %s\nSosa : %s\nD : %s """ % (self.Nom, self.Prenom, self.Sosa , self.DateDeces)
        if self.DateNaissance != None and self.DateDeces != None:
            resultat = """%s %s\nSosa : %s\nN : %s, \nD : %s """ % (self.Nom, self.Prenom, self.Sosa, self.DateNaissance, self.DateDeces)
        return resultat
        # Louis XIV (M, birthday=1638-09-05, deathday=1715-09-01)

    def toJSON(self):
        enfants = []
        for item in self.Enfants:
            enfants.append(item.toJSON())

        result = {
        }
        if self.Sosa != None:
            result['Sosa'] = self.Sosa
        if self.Note != None:
            result['Note'] = self.Note
        if self.Enfants != None:
            result['Enfants'] = enfants
        if self.Religion != None:
            result['Religion'] = self.Religion
        if self.Profession != None:
            result['Profession'] = self.Profession
        if self.PerePresentMariage != None:
            result['PerePresentMariage'] = self.PerePresentMariage
        if self.Aine != None:
            result['Aine'] = self.Aine
        if self.Branche != None:
            result['Branche'] = self.Branche
        if self.Cadet != None:
            result['Cadet'] = self.Cadet
        if self.Nom != None:
            result['Nom'] = self.Nom
        if self.Prenom != None:
            result['Prenom'] = self.Prenom

        if self.LieuNaissance != None:
            result['LieuNaissance'] = str(self.LieuNaissance.toJSON())
        if self.LieuMariage != None:
            result['LieuMariage'] = str(self.LieuMariage.toJSON())
        if self.LieuDeces !=None:
            result['LieuDeces'] = str(self.LieuDeces.toJSON())

        if self.MerePresenteMariage != None:
            result['MerePresenteMariage'] = self.MerePresenteMariage
        if self.Conjoints != None:
            result['Conjoint'] = self.Conjoints

        if self.DateNaissance != None:
            result['DateNaissance'] = str(self.DateNaissance)
        if self.DateMariage != None:
            result['DateMariage'] = str(self.DateMariage)
        if self.DateDeces !=None:
            result['DateDeces'] = str(self.DateDeces)

        if self.Note !=None:
            result['Note'] = self.Note
        if self.Cadet !=None:
            result['Cadet'] = self.Cadet
        if self.Aine !=None:
            result['Aine'] = self.Aine

        if self.AgeDeces !=None:
            result['AgeDeces'] = self.AgeDeces
        if self.ConjointDecedesDeces !=None:
            result['ConjointDecedesDeces'] = self.ConjointDecedesDeces
        return result

    def setPersonne(self, json):
        if 'Sosa' in json:
            self.Sosa = json['Sosa']
            self.setSexe()
        if 'Note' in json:
            self.Note = json['Note']
        if 'Enfants' in json:
            self.Enfants = enfantFromJson(json['Enfants'])
        if 'Religion' in json:
            self.Religion = json['Religion']
        if 'Profession' in json:
            self.Profession = json['Profession']
        if 'PerePresentMariage' in json:
            self.PerePresentMariage = json['PerePresentMariage']
        if 'Aine' in json:
            self.Aine = json['Aine']
        if 'Branche' in json:
            self.Branche = json['Branche']
        if 'Cadet' in json:
            self.Cadet = json['Cadet']
        if 'Nom' in json:
            self.Nom = json['Nom']
        if 'Prenom' in json:
            self.Prenom = json['Prenom']
        if 'LieuNaissance' in json:
            self.LieuNaissance = json['LieuNaissance']
        if 'LieuMariage' in json:
            self.LieuMariage = json['LieuMariage']
        if 'MerePresenteMariage' in json:
            self.MerePresenteMariage = json['MerePresenteMariage']
        if 'Conjoint' in json:
            self.Conjoint = json['Conjoint']
        if 'DateNaissance' in json:
            self.DateNaissance = Date({'key':'DateNaissance', 'value' :json['DateNaissance']})
        if 'DateMariage' in json:
            self.DateMariage = Date({'key':'DateMariage', 'value' :json['DateMariage']})
        if 'DateDeces' in json:
            self.DateDeces = Date({'key':'DateDeces', 'value' :json['DateDeces']})
        if 'Note' in json:
            self.Note = json['Note']
        if 'LieuDeces' in json:
            self.LieuDeces = json['LieuDeces']
        if 'LieuMariage' in json:
            self.LieuMariage = json['LieuMariage']
        if 'LieuNaissance' in json:
            self.LieuNaissance = json['LieuNaissance']
        if 'Conjoints' in json:
            self.Conjoints = json['Conjoints']
        if 'Cadet' in json:
            self.Cadet = json['Cadet']
        if 'Aine' in json:
            self.Aine = json['Aine']
        if 'AgeDeces' in json:
            self.AgeDeces = json['AgeDeces']
        if 'ConjointDecedesDeces' in json:
            self.ConjointDecedesDeces = json['ConjointDecedesDeces']

        return self
