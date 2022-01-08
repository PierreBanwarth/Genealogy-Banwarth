import ttkbootstrap as ttk
from ttkbootstrap.constants import *

PADDING = 10
def plotRepartitionAnnuelle(result):
    test = {}
    for k, v in result.items():
        year = v.getAnneeNaissance()
        if year != None:
            if year not in test:
                test[int(year)] = 1
            else:
                test[int(year)] = test[year]+1
        for item in v.getEnfants():
            if item.getDateNaissance() != None:
                year = item.getAnneeNaissance()
                if year != None:
                    if year not in test:
                        test[year] = 1
                    else:
                        test[year] = test[year]+1
    od = collections.OrderedDict(sorted(test.items()))
    names = []
    values = []

    for k, v in test.items():
        names.append(k)


class StatistiquesLabel():
    def __init__(self, label, treeExplorer):
        self.labelStat = label
        self.treeExplorer = treeExplorer

        self.individus = ttk.Label(self.labelStat, text=str(treeExplorer.getNbIndividus())+' Individus')
        self.labelSosa = ttk.Label(self.labelStat, text=str(treeExplorer.getNbSosa())+' Sosas')
        self.frereEtSoeur = ttk.Label(self.labelStat, text=str(treeExplorer.getNbFrereEttSoeur())+' Frere et Soeur')
        self.mariages = ttk.Label(self.labelStat, text=str(treeExplorer.getNbMariages())+' Mariages')
        self.patronymes = ttk.Label(self.labelStat, text=str(treeExplorer.getNbPatronymes())+' Patronymes')
        self.lieux = ttk.Label(self.labelStat, text=str(treeExplorer.getNbLieux())+' Lieux')
        self.profession = ttk.Label(self.labelStat, text=str(treeExplorer.getNbProfession())+' Professions')


    def pack(self):
        self.individus.pack(side=LEFT, fill=BOTH, expand=1, pady=PADDING, padx=PADDING)
        self.labelSosa.pack(side=LEFT, fill=BOTH, expand=1, pady=PADDING)
        self.frereEtSoeur.pack(side=LEFT, fill=BOTH, expand=1, pady=PADDING)
        self.mariages.pack(side=LEFT, fill=BOTH, expand=1, pady=PADDING)
        self.patronymes.pack(side=LEFT, fill=BOTH, expand=1, pady=PADDING)
        self.lieux.pack(side=LEFT, fill=BOTH, expand=1, pady=PADDING)
        self.profession.pack(side=LEFT, fill=BOTH, expand=1, pady=PADDING)
