from classes.fichiers import *

import json

class Lieu:

    def getFichierRegions(self):
        with open('data/departements-region.json') as json_file:
            lieux = json.load(json_file)
            return lieux

    def getLieuxFromString(self, s):
        if s == '***par jugement':
            return {
                'ville' : 'Inconnu par jugement'
            }
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

    def getIndexLieux(self, s):
        lieu = self.getLieuxFromString(s)
        regions = self.getFichierRegions()
        print(lieu)
        if 'ville' in lieu and lieu['ville'] == 'Inconnu par jugement':
            return lieu

        if 'departement' in lieu:
            for region in regions:
                if str(lieu['departement']) == str(region['num_dep']):
                    lieu['departementName'] = region['dep_name']
                    lieu['regionName'] = region['region_name']
        return lieu



    def __init__(self, s):
        result = self.getIndexLieux(s)

        self.ville = result['ville']
        self.departementNumber = None
        self.region = None
        self.departementName = None
        self.pays = None

        if 'departement' in result:
            self.departementNumber = result['departement']
            self.departementName = result['departementName']
            self.region = result['regionName']

        if 'pays' in result:
            self.pays = result['pays']



    def __str__(self):
        if self.pays == None and self.region == None:
            return self.ville
        if self.pays == None:
            return self.departementName + ' ' + self.ville
        else:
            return self.pays + ' '+self.ville

    def toJSON(self):
        return str(self)
