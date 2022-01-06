


class TreeExplorer():
    def __init__(self, personne, arbre):
        self.arbre = arbre

        self.currentPersonne = arbre[personne]
        print('init')
        print(self.currentPersonne)

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

    def exploreTreeNetworkX(self, id, idOld, G, i):
        if id in self.arbre and i<3:
            G.add_node(id)
            if i>0 and idOld != '':
                G.add_edge(id,idOld)

            self.exploreTreeNetworkX(id*2, id, G, i+1)
            self.exploreTreeNetworkX(id*2+1, id, G, i+1)

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
