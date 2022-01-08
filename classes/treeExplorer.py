


class TreeExplorer():
    def __init__(self, personne, arbre):
        self.arbre = arbre
        self.currentPersonne = arbre[personne]

    def getCurrentPersonne(self):
        return self.currentPersonne

    def getCurrentPersonneSosa(self):
        return self.currentPersonne.Sosa

    def getEnfants(self):
        return self.currentPersonne.Enfants

    def goToMere(self):
        return self.goTo(self.currentPersonne.getMere())

    def goToPere(self):
        return self.goTo(self.currentPersonne.getPere())

    def goToHeritier(self):
        return self.goTo(self.currentPersonne.getHeritier())
    def goToConjoint(self):
        return self.goTo(self.currentPersonne.getConjointSosa())

    def goToSosa(self, sosa):
        return self.goTo(sosa)

    def getMere(self):
        return self.get(self.currentPersonne.getMere())

    def getConjoint(self):
        return self.get(self.currentPersonne.getConjointSosa())

    def getBeauPapa(self):
        return self.get(self.currentPersonne.getBeauPapa())

    def getBelleMaman(self):
        return self.get(self.currentPersonne.getBelleMaman())

    def getPere(self):
        return self.get(self.currentPersonne.getPere())

    def getHeritier(self):
        return self.get(self.currentPersonne.getHeritier())
    def getFratrie(self):
        result = []
        pere = self.getPere()
        for item in pere.getEnfants():
            if item.Sosa == None:
                result.append(item)
        return result

    def exploreTreeNetworkX(self, id, idOld, G, i):
        if id in self.arbre and i<3:
            G.add_node(id)
            if i>0 and idOld != '':
                G.add_edge(id,idOld)

            self.exploreTreeNetworkX(id*2, id, G, i+1)
            self.exploreTreeNetworkX(id*2+1, id, G, i+1)

    def getNbIndividus(self):
        result = 0
        for item in self.arbre:
            result = result + 1
            # On regarde le nombre d'enfant des hommes de la famille
            if item%2 ==0 and self.arbre[item].Enfants !=None:
                result =result+len(self.get(item).Enfants)
        return result

    def getNbFrereEttSoeur(self):
        result = 0
        for item in self.arbre:
            # On regarde le nombre d'enfant des hommes de la famille
            if item%2 ==0 and self.arbre[item].Enfants !=None:
                result =result+len(self.get(item).Enfants)
        return result

    def getNbMariages(self):
        result = 0
        for item in self.arbre:
            # On regarde le nombre d'enfant des hommes de la famille
            if item%2 ==0 and item+1 in self.arbre:
                result = result+1
        return result

    def getNbPatronymes(self):
        result = []
        for item in self.arbre:
            if self.arbre[item].Nom != None:
                if self.arbre[item].Nom not in result:
                    result.append(self.arbre[item].Nom)
        return len(result)

    def getNbLieux(self):
        result = []
        for item in self.arbre:
            if self.arbre[item].LieuDeces != None:
                if self.arbre[item].LieuDeces not in result:
                    result.append(self.arbre[item].LieuDeces)
            if self.arbre[item].LieuNaissance != None:
                if self.arbre[item].LieuNaissance not in result:
                    result.append(self.arbre[item].LieuNaissance)
            if self.arbre[item].LieuMariage != None:
                if self.arbre[item].LieuMariage not in result:
                    result.append(self.arbre[item].LieuMariage)
        return len(result)

    def getNbProfession(self):
        result = []
        for item in self.arbre:
            if self.arbre[item].Profession != None:
                if self.arbre[item].Profession not in result:
                    result.append(self.arbre[item].Profession)
        return len(result)

    def getNbSosa(self):
        return len(self.arbre)

    def getLabels(self, list):
        result = {}
        for item in list:
            if item in self.arbre:
                result[item] = self.arbre[item].getDisplayStr()
        return result

    def get(self, index):
        if index in self.arbre:
            return self.arbre[index]
        else:
            return None

    def goTo(self, index):
        if index in self.arbre:
            self.currentPersonne = self.arbre[index]
            return True
        else:
            return False
