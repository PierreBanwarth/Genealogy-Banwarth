import datetime # we will use this for date objects

class Person:

    def __init__(self, json):

        self.Branche = json['Branche']

        if 'Aine' in json:
            self.Aine = json['Aine']
        else:
            self.Aine = 'Unkown'

        if 'Cadet' in json:
            self.Cadet = json['Cadet']
        else:
            self.Cadet = 'Unkown'

        if 'MerePresentMariage' in json:
            self.MerePresentMariage = json['MerePresentMariage']
        else:
            self.MerePresentMariage = 'Unkown'

        if 'PerePresentMariage' in json:
            self.PerePresentMariage = json['PerePresentMariage']
        else:
            self.PerePresentMariage = 'Unkown'

        if 'Note' in json:
            self.Note = json['Note']
        else:
            self.Note = 'Unkown'

        if 'DateMariage' in json:
            self.DateMariage = json['DateMariage']
        else:
            self.DateMariage = 'Unkown'

        if 'DateDeces' in json:
            self.DateDeces = json['DateDeces']
        else:
            self.DateDeces = 'Unkown'

        if 'LieuMariage' in json:
            self.LieuMariage = json['LieuMariage']
        else:
            self.LieuMariage = 'Unkown'

        if 'Religion' in json:
            self.Religion = json['Religion']
        else:
            self.Religion = 'Unkown'

        if 'Profession' in json:
            self.Profession = json['Profession']
        else:
            self.Profession = 'Unkown'

        if 'DateNaissance' in json:
            self.DateNaissance = json['DateNaissance']
        else:
            self.DateNaissance = 'Unkown'

        if 'LieuNaissance' in json:
            self.LieuNaissance = json['LieuNaissance']
        else:
            self.LieuNaissance = 'Unkown'

        if 'Nom' in json:
            self.Nom = json['Nom']
        else:
            self.Nom = 'Unkown'
        if 'Prenom' in json:
            self.Prenom = json['Prenom']
        else:
            self.Nom = 'Unkown'

        self.Sosa = int(json['Sosa'])

        if (self.Sosa % 2) == 0:
            self.Male = True
        else:
            self.Male = False

        self.conjoints = json['conjoints']
        self.enfants = json['enfants']

    def getSonSosa(self):
        if self.Sosa <= 3:
            return self.Sosa
        if (self.Sosa % 2) == 0:
            return int(self.Sosa/2)
        else:
            return int((self.Sosa-1)/2)

    def isToFindSon(self):
        print(self.enfants)
        return 'Sosa' in self.enfants[0] and self.enfants[0]['Sosa']

    def addAine(self, person):
        self.enfants.pop(0)
        self.enfants.insert(0,person.getInfoHeritier())

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
            'Aine' : self.Aine,
            'Branche' : self.Branche,
            'Cadet' : self.Cadet,
            'DateMariage' : self.DateMariage,
            'DateNaissance' : self.DateNaissance,
            'DateDeces' : self.DateDeces,
            'LieuMariage' : self.LieuMariage,
            'LieuNaissance' : self.LieuNaissance,
            'Nom' : self.Nom,
            'Note' : self.Note,
            'PerePresentMariage' : self.PerePresentMariage,
            'MerePresentMariage' : self.MerePresentMariage,
            'Prenom' : self.Prenom,
            'Profession' : self.Profession,
            'Religion' : self.Religion,
            'Sosa' : self.Sosa,
            'conjoints' : self.conjoints,
            'enfants' : self.enfants
        }
