import datetime # we will use this for date objects
from tkinter import *
import ttkbootstrap as ttk

from classes.personne import Personne

from PIL import Image, ImageTk

class ParentLabel():
    def __init__(self, labelPere):

        self.textSosa = StringVar()
        self.textNom = StringVar()
        self.textDateNaissance = StringVar()
        self.textLieuNaissance = StringVar()
        self.textDeces =StringVar()
        self.textLieuDeces =StringVar()
        self.textAge = StringVar()
        self.textProfession = StringVar()

        self.labelSosa = ttk.Label(labelPere, textvariable=self.textSosa)
        self.labelNom = ttk.Label(labelPere, textvariable=self.textNom )
        self.labelNaissance = ttk.Label(labelPere, textvariable=self.textDateNaissance)
        self.labelLieuNaissance = ttk.Label(labelPere, textvariable=self.textLieuNaissance)
        self.labelDeces = ttk.Label(labelPere, textvariable=self.textDeces)
        self.labelLieuDeces = ttk.Label(labelPere, textvariable=self.textLieuDeces)
        self.labelAge = ttk.Label(labelPere, textvariable=self.textDateNaissance)
        self.labelProfession = ttk.Label(labelPere, textvariable=self.textProfession)


    def pack(self):
        self.labelSosa.pack(fill=BOTH,expand=1)
        self.labelNom.pack(fill=BOTH,expand=1)
        self.labelNaissance.pack(fill=BOTH,expand=1)
        self.labelLieuNaissance.pack(fill=BOTH,expand=1)
        self.labelDeces.pack(fill=BOTH,expand=1)
        self.labelLieuDeces.pack(fill=BOTH,expand=1)
        self.labelProfession.pack(fill=BOTH,expand=1)
        self.labelProfession.pack(fill=BOTH,expand=1)

    def set(self, personne):

        if personne.Nom != None and personne.Prenom != None:
            self.textNom.set('Nom :'+personne.Nom +' '+personne.Prenom)
        else:
            self.textNom.set('-')

        if personne.Sosa != None:
            self.textSosa.set(str(personne.Sosa))
        else:
            self.textSosa.set('-')

        if personne.DateNaissance != None:
            self.textDateNaissance.set('Date de Naissance : '+str(personne.DateNaissance))
        else:
            self.textDateNaissance.set('-')

        if personne.LieuNaissance != None:
            self.textLieuNaissance.set('Lieu de Naissance : '+personne.LieuNaissance)
        else:
            self.textLieuNaissance.set('-')

        if personne.DateDeces != None:
            self.textDeces.set('Date de deces : '+str(personne.DateDeces))
        else:
            self.textDeces.set('-')

        if personne.LieuDeces != None:
            self.textLieuDeces.set('Lieu de deces : '+personne.LieuDeces)
        else:
            self.textLieuDeces.set('-')

        if personne.Profession != None:
            self.textProfession.set('Profession : '+personne.Profession)
        else:
            self.textProfession.set('-')

class EnfantLabel():

    def __init__(self, labelEnfant):
        self.textNom = StringVar()
        self.textDateNaissance = StringVar()
        self.textDateDeces =StringVar()
        self.textDateMariage =StringVar()
        self.textSosa =StringVar()

        self.labelNom = Label(labelEnfant, textvariable=self.textNom)
        self.labelDateNaissance = Label(labelEnfant, textvariable=self.textDateNaissance)
        self.labelDateDeces = Label(labelEnfant, textvariable=self.textDateDeces)
        self.labelDateMariage = Label(labelEnfant, textvariable=self.textDateMariage)
        self.labelSosa = Label(labelEnfant, textvariable=self.textSosa)


    def set(self, enfant):
        if enfant.Prenom != None:
            self.textNom.set(enfant.Prenom)
        else:
            self.textNom.set('-')

        if enfant.DateNaissance != None:
            self.textDateNaissance.set(enfant.DateNaissance)
        else:
            self.textDateNaissance.set('-')

        if enfant.DateMariage != None:
            self.textDateMariage.set(enfant.DateMariage)
        else:
            self.textDateMariage.set('-')

        if enfant.DateDeces != None:
            self.textDateDeces.set(enfant.DateDeces)
        else:
            self.textDateDeces.set('-')

        if enfant.Sosa != None:
            self.textSosa.set(enfant.Sosa)
        else:
            self.textSosa.set('-')

    def pack(self):
        self.labelNom.pack()
        self.labelDateNaissance.pack()
        self.labelDateDeces.pack()
        self.labelDateMariage.pack()
        self.labelSosa.pack()

    def destroy(self):
        self.labelNom.destroy()
        self.labelDateNaissance.destroy()
        self.labelDateDeces.destroy()
        self.labelDateMariage.destroy()
        self.labelSosa.destroy()

class MariageLabel():
    def __init__(self, labelMariage):
        self.textSosa = StringVar()
        self.textNomEpouse = StringVar()
        self.textDateMariage = StringVar()
        self.textLieuMariage =StringVar()
        self.textPapaMarie =StringVar()
        self.textMamanMarie =StringVar()

        self.labelSosa = Label(labelMariage,  textvariable=self.textSosa)
        self.labelNomEpouse = Label(labelMariage,  textvariable=self.textNomEpouse)
        self.labelDateMariage = Label(labelMariage,  textvariable=self.textDateMariage)
        self.labelLieuMariage =Label(labelMariage,  textvariable=self.textLieuMariage)
        self.labelPapaMarie =Label(labelMariage,  textvariable=self.textPapaMarie)
        self.labelMamanMarie =Label(labelMariage,  textvariable=self.textMamanMarie)

    def pack(self):
        self.labelSosa.pack()
        self.labelNomEpouse.pack()
        self.labelDateMariage.pack()
        self.labelLieuMariage.pack()
        self.labelPapaMarie.pack()
        self.labelMamanMarie.pack()

    def set(self, personne, conjoint, papa, maman):

        if papa.Prenom != None and papa.Nom != None:
            self.textPapaMarie.set(papa.Nom +' '+papa.Prenom)
        else:
            self.textPapaMarie.set('-')

        if maman.Prenom != None and maman.Nom != None:
            self.textMamanMarie.set(maman.Nom +' '+maman.Prenom)
        else:
            self.textMamanMarie.set('-')

        if conjoint.Prenom != None and conjoint.Nom != None:
            self.textNomEpouse.set(conjoint.Nom +' '+conjoint.Prenom)
        else:
            self.textNomEpouse.set('-')

        if personne.DateMariage != None:
            self.textDateMariage.set(personne.DateMariage)
        else:
            self.textDateMariage.set('-')

        if personne.LieuMariage != None:
            self.textLieuMariage.set(personne.LieuMariage)
        else:
            self.textLieuMariage.set('-')

        if conjoint.Sosa != None:
            self.textSosa.set(conjoint.Sosa)
        else:
            self.textSosa.set('-')

class EnfantLabelListe():

    def __init__(self, labelEnfant):
        self.enfantListe = []
        self.labelEnfant = labelEnfant

    def pack(self):
        for item in self.enfantListe:
            item.pack()

    def set(self, listEnfant):

        if len(listEnfant) == 0:
            self.sansEnfant = Label(self.labelEnfant,  text='Sans enfants')
            self.sansEnfant.pack()
        else:
            self.sansEnfant.destroy()

            for item in self.enfantListe:
                item.destroy()
            self.enfantListe=[]
            for item in listEnfant:
                newEnfant = EnfantLabel(self.labelEnfant)
                newEnfant.set(item)
                newEnfant.pack()
                self.enfantListe.append(newEnfant)



class PersonneLabel():
    def __init__(self, labelPersonne, labelEnfant, labelPere, labelMere, labelMariage, treeExplorer):

        self.labelPersonne = labelPersonne
        self.labelEnfant = labelEnfant
        self.labelPere = labelPere
        self.labelMere = labelMere
        self.labelMariage = labelMariage

        personnePere = treeExplorer.getPere()
        personneMere = treeExplorer.getMere()
        enfants = treeExplorer.getEnfants()
        personne = treeExplorer.getCurrentPersonne()
        #
        # personne.DateMariage = None
        # personne.LieuMariage = None

        self.Personne = ParentLabel(self.labelPersonne)
        self.Enfants = EnfantLabelListe(self.labelEnfant)
        self.Pere = ParentLabel(self.labelPere)
        self.Mere = ParentLabel(self.labelMere)
        self.Mariage = MariageLabel(self.labelMariage)


    def pack(self):

        self.Personne.pack()
        self.Pere.pack()
        self.Mere.pack()
        self.Mariage.pack()
        self.Enfants.pack()

    def set(self, treeExplorer):
        personnePere = treeExplorer.getPere()
        personneMere = treeExplorer.getMere()
        enfants = treeExplorer.getEnfants()
        conjoint = treeExplorer.getConjoint()
        beauPapa = treeExplorer.getBeauPapa()
        belleMaman = treeExplorer.getBelleMaman()
        personne = treeExplorer.getCurrentPersonne()

        self.Pere.set(personnePere)
        self.Mere.set(personneMere)
        self.Personne.set(personne)
        self.Mariage.set(personne, conjoint, beauPapa, belleMaman)
        self.Enfants.set(enfants)
