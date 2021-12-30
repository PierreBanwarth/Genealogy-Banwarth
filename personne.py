import datetime # we will use this for date objects
import json

astro = [
    {'signe' : 'Belier', 'dateDebut' : '21/03', 'dateFin' : '19/04'},
    {'signe' : 'Taureau', 'dateDebut' : '20/04', 'dateFin' : '20/05'},
    {'signe' : 'Gemeaux', 'dateDebut' : '21/05', 'dateFin' : '21/06'},
    {'signe' : 'Cancer', 'dateDebut' : '22/06', 'dateFin' : '22/07'},
    {'signe' : 'Lion', 'dateDebut' : '23/07', 'dateFin' : '22/08'},
    {'signe' : 'Vierge', 'dateDebut' : '23/08', 'dateFin' : '22/09'},
    {'signe' : 'Balance', 'dateDebut' : '23/09', 'dateFin' : '23/10'},
    {'signe' : 'Scorpion', 'dateDebut' : '24/10', 'dateFin' : '22/11'},
    {'signe' : 'Sagittaire', 'dateDebut' : '23/11', 'dateFin' : '22/12'},
    {'signe' : 'Capricorne', 'dateDebut' : '23/12', 'dateFin' : '20/01'},
    {'signe' : 'Verseau', 'dateDebut' : '21/01', 'dateFin' : '19/02'},
    {'signe' : 'Poissons', 'dateDebut' : '20/02', 'dateFin' : '20/03'}
]

regnes = [
    {'nom' : 'Clovis Ier', 'dateDebut':'481','dateFin': '511'},
    {'nom' : 'Clotaire Ier', 'dateDebut':'511','dateFin': '561'},
    {'nom' : 'Chilperic Ier', 'dateDebut':'561','dateFin': '584'},
    {'nom' : 'Clotaire II', 'dateDebut':'584','dateFin': '629'},
    {'nom' : 'Dagobert Ier', 'dateDebut':'629','dateFin': '639'},
    {'nom' : 'Clovis II', 'dateDebut':'639','dateFin': '657'},
    {'nom' : '''Childebert III l'Adopte''', 'dateDebut':'657', 'dateFin': '662'},
    {'nom' : 'Childeric II', 'dateDebut':'662','dateFin': '675'},
    {'nom' : 'Thierry III', 'dateDebut':'675','dateFin': '691'},
    {'nom' : 'Clovis IV', 'dateDebut':'691','dateFin': '695'},
    {'nom' : 'Childebert IV', 'dateDebut':'695','dateFin': '711'},
    {'nom' : 'Dagobert III', 'dateDebut':'711','dateFin': '715'},
    {'nom' : 'Chilperic II', 'dateDebut':'715','dateFin': '721'},
    {'nom' : 'Thierry IV', 'dateDebut':'721','dateFin': '737'},
    {'nom' : 'Childeric III', 'dateDebut':'743','dateFin': '751'},
    {'nom' : 'Pepin le Bref', 'dateDebut':'751','dateFin': '768'},
    {'nom' : 'Charlemagne', 'dateDebut':'768','dateFin': '814'},
    {'nom' : 'Louis le Pieux', 'dateDebut':'814','dateFin': '840'},
    {'nom' : 'Charles II le Chauve', 'dateDebut':'843','dateFin': '877'},
    {'nom' : 'Louis II le Begue', 'dateDebut':'877','dateFin': '879'},
    {'nom' : 'Louis III', 'dateDebut':'879','dateFin': '882'},
    {'nom' : 'Carloman II', 'dateDebut':'879','dateFin': '884'},
    {'nom' : 'Charles III le Gros', 'dateDebut':'884','dateFin': '887'},
    {'nom' : 'Eudes', 'dateDebut':'888','dateFin': '898'},
    {'nom' : 'Charles III le Simple', 'dateDebut':'893','dateFin': '923'},
    {'nom' : 'Raoul', 'dateDebut':'923','dateFin': '936'},
    {'nom' : '''Louis IV d'Outremer''', 'dateDebut':'936','dateFin': '954'},
    {'nom' : 'Lothaire', 'dateDebut':'954','dateFin': '986'},
    {'nom' : 'Louis V le Faineant', 'dateDebut':'986','dateFin': '987'},
    {'nom' : 'Hugues Capet', 'dateDebut':'987','dateFin': '996'},
    {'nom' : 'Robert II le Pieux', 'dateDebut':'996','dateFin': '1031'},
    {'nom' : 'Henri Ier', 'dateDebut':'1031','dateFin': '1060'},
    {'nom' : 'Philippe Ier', 'dateDebut':'1060','dateFin': '1108'},
    {'nom' : 'Louis VI le Gros', 'dateDebut':'1108','dateFin': '1137'},
    {'nom' : 'Louis VII le Jeune', 'dateDebut':'1137','dateFin': '1180'},
    {'nom' : 'Philippe II Auguste', 'dateDebut':'1180','dateFin': '1223'},
    {'nom' : 'Louis VIII le Lion', 'dateDebut':'1223','dateFin': '1226'},
    {'nom' : 'Louis IX', 'dateDebut':'1226','dateFin': '1270'},
    {'nom' : 'Philippe III le Hardi', 'dateDebut':'1270','dateFin': '1285'},
    {'nom' : 'Philippe IV le Bel', 'dateDebut':'1285','dateFin': '1314'},
    {'nom' : 'Louis X', 'dateDebut':'1314','dateFin': '1316'},
    {'nom' : 'Jean Ier le Posthume', 'dateDebut':'1316','dateFin': '1316'},
    {'nom' : 'Philippe V le Long', 'dateDebut':'1316','dateFin': '1322'},
    {'nom' : 'Charles IV le Bel', 'dateDebut':'1322','dateFin': '1328'},
    {'nom' : 'Philippe VI de Valois', 'dateDebut':'1328','dateFin': '1350'},
    {'nom' : 'Jean II le Bon', 'dateDebut':'1350','dateFin': '1364'},
    {'nom' : 'Charles V le Sage', 'dateDebut':'1364','dateFin': '1380'},
    {'nom' : 'Charles VI', 'dateDebut':'1380','dateFin': '1422'},
    {'nom' : 'Charles VII', 'dateDebut':'1422','dateFin': '1461'},
    {'nom' : 'Louis XI', 'dateDebut':'1461','dateFin': '1483'},
    {'nom' : 'Charles VIII', 'dateDebut':'1483','dateFin': '1498'},
    {'nom' : 'Louis XII', 'dateDebut':'1498','dateFin': '1515'},
    {'nom' : 'François Ier', 'dateDebut':'1515','dateFin': '1547'},
    {'nom' : 'Henri II', 'dateDebut':'1547','dateFin': '1559'},
    {'nom' : 'François II', 'dateDebut':'1559','dateFin': '1560'},
    {'nom' : 'Charles IX', 'dateDebut':'1560','dateFin': '1574'},
    {'nom' : 'Henri III', 'dateDebut':'1574','dateFin': '1589'},
    {'nom' : 'Henri IV', 'dateDebut':'1589','dateFin': '1610'},
    {'nom' : 'Louis XIII', 'dateDebut':'1610','dateFin': '1643'},
    {'nom' : 'Louis XIV', 'dateDebut':'1643','dateFin': '1715'},
    {'nom' : 'Louis XV', 'dateDebut':'1715','dateFin': '1774'},
    {'nom' : 'Louis XVI', 'dateDebut':'1774','dateFin': '1792'},
    {'nom' : 'Convention', 'dateDebut':'1792','dateFin': '1793'},
    {'nom' : 'Comite de salut public', 'dateDebut':'1793','dateFin': '1794'},
    {'nom' : 'Convention', 'dateDebut':'1794','dateFin': '1795'},
    {'nom' : 'Directoire', 'dateDebut':'1795','dateFin': '1799'},
    {'nom' : 'Premier consul Napoleon Bonaparte', 'dateDebut':'1799','dateFin': '1804'},
    {'nom' : 'Napoleon Ier', 'dateDebut':'1804','dateFin': '1815'},
    {'nom' : 'Napoleon II', 'dateDebut':'1815','dateFin': '1815'},
    {'nom' : 'Louis XVIII', 'dateDebut':'1814','dateFin': '1824'},
    {'nom' : 'Charles X', 'dateDebut':'1824','dateFin': '1830'},
    {'nom' : 'Henri V', 'dateDebut':'1830','dateFin': '1830'},
    {'nom' : 'Louis-Philippe Ier', 'dateDebut':'1830','dateFin': '1848'},
    {'nom' : 'Louis-Napoleon Bonaparte', 'dateDebut':'1848','dateFin': '1852'},
    {'nom' : 'Napoleon III', 'dateDebut':'1852','dateFin': '1870'},
    {'nom' : 'Adolphe Thiers', 'dateDebut':'1871','dateFin': '1873'},
    {'nom' : 'Patrice de Mac Mahon', 'dateDebut':'1873','dateFin': '1879'},
    {'nom' : 'Jules Grevy', 'dateDebut':'1879','dateFin': '1887'},
    {'nom' : 'Sadi Carnot', 'dateDebut':'1887','dateFin': '1894'},
    {'nom' : 'Jean Casimir-Perier', 'dateDebut':'1894','dateFin': '1895'},
    {'nom' : 'Felix Faure', 'dateDebut':'1895','dateFin': '1899'},
    {'nom' : 'emile Loubet', 'dateDebut':'1899','dateFin': '1906'},
    {'nom' : 'Armand Fallieres', 'dateDebut':'1906','dateFin': '1913'},
    {'nom' : 'Raymond Poincare', 'dateDebut':'1913','dateFin': '1920'},
    {'nom' : 'Paul Deschanel', 'dateDebut':'1920','dateFin': '1920'},
    {'nom' : 'Alexandre Millerand', 'dateDebut':'1920','dateFin': '1924'},
    {'nom' : 'Gaston Doumergue', 'dateDebut':'1924','dateFin': '1931'},
    {'nom' : 'Paul Doumer', 'dateDebut':'1931','dateFin': '1932'},
    {'nom' : 'Albert Lebrun', 'dateDebut':'1932','dateFin': '1940'},
    {'nom' : 'Philippe Petain', 'dateDebut':'1940','dateFin': '1944'},
    {'nom' : 'Vincent Auriol', 'dateDebut':'1947','dateFin': '1954'},
    {'nom' : 'Rene Coty', 'dateDebut':'1954','dateFin': '1958'},
    {'nom' : 'Charles de Gaulle', 'dateDebut':'1958','dateFin': '1969'},
    {'nom' : 'Georges Pompidou', 'dateDebut':'1969','dateFin': '1974'},
    {'nom' : '''Valery Giscard d'Estaing''', 'dateDebut':'1974','dateFin': '1981'},
    {'nom' : 'François Mitterrand', 'dateDebut':'1981','dateFin': '1995'},
    {'nom' : 'Jacques Chirac', 'dateDebut':'1995','dateFin': '2007'},
    {'nom' : 'Nicolas Sarkozy', 'dateDebut':'2007','dateFin': '2012'},
    {'nom' : 'François Hollande', 'dateDebut':'2012','dateFin': '2017'},
    {'nom' : 'Emmanuel Macron', 'dateDebut':'2017','dateFin': '2022'}
]




class Personne:

    def getRegnes(self):
        regnesPersonne = []
        if self.DateNaissance != 'Unknown' and self.DateDeces != 'Unknown' and len(self.DateNaissance.split('/')) == 3 and len(self.DateDeces.split('/')) == 3:
            D = self.DateDeces.split('/')[2]
            N = self.DateNaissance.split('/')[2]

            for regne in regnes:
                    Dr = regne['dateDebut']
                    Fr = regne['dateFin']
                    if int(Dr) >= int(D) and int(D)>=int(Fr):
                        regnesPersonne.append(regne)
                    if int(Dr) >= int(N) and int(D)>=int(Fr):
                        regnesPersonne.append(regne)
        print(regnesPersonne)

    def getSigneAstro(self):
        date = self.DateNaissance
        dateArray = date.split('/')
        jour = int(dateArray[0])
        mois = int(dateArray[1])
        finded= False
        for signe in astro:
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
            self.Aine = 'Unkown'

        if 'Cadet' in json:
            self.Cadet = json['Cadet']
        else:
            self.Cadet = 'Unkown'

        if 'LieuDeces' in json:
            self.LieuDeces = json['LieuDeces']
        else:
            self.LieuDeces = 'Unknown'


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

        if 'DateNaissance' in json:
            self.DateNaissance = json['DateNaissance']
        else:
            self.DateNaissance = 'Unkown'

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
# "departement": "57",
# "departementName": "Moselle",
# "regionName": "Grand Est",
# "ville": "BAUDRECOURT"

    def getAge(self):
        return 'Todo calcul age'

    def getLieuNaissance(self):
        if self.LieuNaissance != 'Unknown':
            with open('data/lieux.json') as json_file:
                lieux = json.load(json_file)
                DictLieux = lieux[int(self.LieuNaissance)]
                return DictLieux['ville']+' '+ DictLieux['departementName']+'('+DictLieux['departement']+')'
        else:
            return self.lieuNaissance

    def getLieuDeces(self):
        if self.LieuDeces != 'Unknown':
            with open('data/lieux.json') as json_file:
                lieux = json.load(json_file)
                DictLieux = lieux[int(self.LieuDeces)]
                return DictLieux['ville']+' '+ DictLieux['departementName']+'('+DictLieux['departement']+')'
        else:
            return self.LieuDeces
    def getLieuMariage(self):
        if self.LieuMariage != 'Unknown':

            with open('data/lieux.json') as json_file:
                lieux = json.load(json_file)
                DictLieux = lieux[int(self.LieuMariage)]

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
