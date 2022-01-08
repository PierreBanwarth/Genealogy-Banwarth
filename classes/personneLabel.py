import datetime # we will use this for date objects
from tkinter import *
import ttkbootstrap as ttk

from classes.personne import Personne

from PIL import Image, ImageTk

PADDING=10

def setAttrib(personneAttrib, string ,label):
    if personneAttrib != None:
        label.set(string+' '+str(personneAttrib))
    else:
        label.set('-')

def setMultiAttrb(personneAttrib, personneAttrib2, string ,label):

    if personneAttrib != None and personneAttrib2 != None:
        label.set(string+' '+str(personneAttrib)+' '+str(personneAttrib2))
    else:
        label.set('-')

def setOrDestroy(text, label):
    if '-' != text.get():
        label.pack()
    else:
        label.destroy()

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
        self.textSigneAstro = StringVar()
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
        setMultiAttrb(personne.Nom, personne.Prenom, 'Nom :',self.textNom)
        setAttrib(personne.Sosa, 'Sosa :', self.textSosa)
        setAttrib(personne.DateNaissance, 'Date de Naissance :', self.textDateNaissance)
        setAttrib(personne.LieuNaissance, 'Lieu de Naissance :', self.textLieuNaissance)
        setAttrib(personne.DateDeces, 'Date de Deces :', self.textDeces)
        setAttrib(personne.LieuDeces, 'Lieu De Deces :', self.textLieuDeces)
        setAttrib(personne.Profession, 'Profession :', self.textProfession)

class PersonnageLabel():

    def __init__(self, labelPere):

        self.textSosa = StringVar()
        self.textNom = StringVar()
        self.textDateNaissance = StringVar()
        self.textLieuNaissance = StringVar()
        self.textDeces =StringVar()
        self.textLieuDeces =StringVar()
        self.textAge = StringVar()
        self.textProfession = StringVar()
        self.textSigneAstro = StringVar()

        self.Gauche = ttk.Frame(labelPere)
        self.Droite = ttk.Frame(labelPere)

        self.labelSigneAstro = ttk.Label(self.Gauche, textvariable=self.textSigneAstro)
        self.labelSosa = ttk.Label(self.Gauche, textvariable=self.textSosa)
        self.labelNom = ttk.Label(self.Gauche, textvariable=self.textNom )
        self.labelNaissance = ttk.Label(self.Gauche, textvariable=self.textDateNaissance)
        self.labelLieuNaissance = ttk.Label(self.Gauche, textvariable=self.textLieuNaissance)
        self.labelDeces = ttk.Label(self.Gauche, textvariable=self.textDeces)
        self.labelLieuDeces = ttk.Label(self.Gauche, textvariable=self.textLieuDeces)
        self.labelAge = ttk.Label(self.Gauche, textvariable=self.textDateNaissance)
        self.labelProfession = ttk.Label(self.Gauche, textvariable=self.textProfession)
        self.noteTextLabel = ttk.Text(self.Droite, height=5, width=50)

    def pack(self):
        self.labelSosa.pack(fill=BOTH,expand=1)
        self.labelNom.pack(fill=BOTH,expand=1)
        self.labelNaissance.pack(fill=BOTH,expand=1)
        self.labelLieuNaissance.pack(fill=BOTH,expand=1)
        self.labelDeces.pack(fill=BOTH,expand=1)
        self.labelLieuDeces.pack(fill=BOTH,expand=1)
        self.labelProfession.pack(fill=BOTH,expand=1)
        self.labelProfession.pack(fill=BOTH,expand=1)
        self.labelSigneAstro.pack(fill=BOTH,expand=1)
        self.noteTextLabel.pack(fill=BOTH,expand=1)
        self.Droite.pack(side=RIGHT,fill=BOTH,expand=1, padx=PADDING, pady=PADDING)
        self.Gauche.pack(side=LEFT,fill=BOTH,expand=1, padx=PADDING, pady=PADDING)

    def set(self, personne):
        self.noteTextLabel.delete(1.0,END)
        setMultiAttrb(personne.Nom, personne.Prenom, 'Nom :',self.textNom)
        setAttrib(personne.Sosa, 'Sosa :', self.textSosa)
        setAttrib(personne.DateNaissance, 'Date de Naissance :', self.textDateNaissance)
        setAttrib(personne.LieuNaissance, 'Lieu de Naissance :', self.textLieuNaissance)
        setAttrib(personne.DateDeces, 'Date de Deces :', self.textDeces)
        setAttrib(personne.LieuDeces, 'Lieu De Deces :', self.textLieuDeces)
        setAttrib(personne.Profession, 'Profession :', self.textProfession)
        setAttrib(personne.getSigneAstro(), 'Signe Astrologique :', self.textSigneAstro)

        if personne.Note != None:
             self.noteTextLabel.insert(INSERT,str(personne.Note))
        else:
             self.noteTextLabel.insert(INSERT,'-')

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
        setAttrib(enfant.Prenom, 'Prenom :', self.textNom)
        setAttrib(enfant.DateNaissance, 'Date de Naissance :', self.textDateNaissance)
        setAttrib(enfant.DateMariage, 'Date de Mariage :', self.textDateMariage)
        setAttrib(enfant.DateDeces, 'Date de Deces :', self.textDateDeces)
        setAttrib(enfant.Sosa, 'Sosa :', self.textSosa)

    def pack(self):
        setOrDestroy(self.textNom, self.labelNom)
        setOrDestroy(self.textDateNaissance, self.labelDateNaissance)
        setOrDestroy(self.textDateDeces, self.labelDateDeces)
        setOrDestroy(self.textDateMariage, self.labelDateMariage)
        setOrDestroy(self.textSosa, self.labelSosa)

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
        setOrDestroy(self.textSosa, self.labelSosa)
        setOrDestroy(self.textNomEpouse, self.labelNomEpouse)
        setOrDestroy(self.textDateMariage, self.labelDateMariage)
        setOrDestroy(self.textLieuMariage, self.labelLieuMariage)
        setOrDestroy(self.textPapaMarie, self.labelPapaMarie)
        setOrDestroy(self.textMamanMarie, self.labelMamanMarie)


    def set(self, personne, conjoint, papa, maman):
        setMultiAttrb(papa.Nom, papa.Prenom, 'Beau Papa :',self.textPapaMarie)
        setMultiAttrb(maman.Nom, maman.Prenom, 'Belle Maman :',self.textMamanMarie)
        setMultiAttrb(conjoint.Nom, conjoint.Prenom, 'Conjoint :',self.textNomEpouse)
        setAttrib(personne.DateMariage, 'Date Mariage : ', self.textDateMariage)
        setAttrib(personne.LieuMariage, 'Lieu Mariage : ', self.textLieuMariage)
        setAttrib(personne.Sosa, 'Sosa : ', self.textSosa)



class EnfantLabelListe():

    def __init__(self, labelEnfant, str):
        self.enfantListe = []
        self.labelEnfant = labelEnfant
        self.sansEnfant = Label(self.labelEnfant,  text=str)
    def pack(self):
        for item in self.enfantListe:
            item.pack()

    def set(self, listEnfant):

        if len(listEnfant) == 0:
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
    def __init__(self, labelPersonne, labelEnfant, labelPere, labelMere, labelMariage, labelFratrie, treeExplorer):

        self.labelPersonne = labelPersonne
        self.labelEnfant = labelEnfant
        self.labelPere = labelPere
        self.labelMere = labelMere
        self.labelMariage = labelMariage
        self.labelFratrie = labelFratrie


        # personne.DateMariage = None
        # personne.LieuMariage = None
        self.Fratrie = EnfantLabelListe(self.labelFratrie, 'Pas de Frere et Soeur')
        self.Enfants = EnfantLabelListe(self.labelEnfant, '''Pas d'enfants''')

        self.Personne = PersonnageLabel(self.labelPersonne)
        self.Pere = ParentLabel(self.labelPere)
        self.Mere = ParentLabel(self.labelMere)
        self.Mariage = MariageLabel(self.labelMariage)


    def pack(self):

        self.Personne.pack()
        self.Pere.pack()
        self.Mere.pack()
        self.Mariage.pack()
        self.Enfants.pack()
        self.Fratrie.pack()

    def set(self, treeExplorer):
        personnePere = treeExplorer.getPere()
        personneMere = treeExplorer.getMere()
        enfants = treeExplorer.getEnfants()
        conjoint = treeExplorer.getConjoint()
        beauPapa = treeExplorer.getBeauPapa()
        belleMaman = treeExplorer.getBelleMaman()
        personne = treeExplorer.getCurrentPersonne()
        fratrie = treeExplorer.getFratrie()
        self.Pere.set(personnePere)
        self.Mere.set(personneMere)
        self.Personne.set(personne)
        self.Mariage.set(personne, conjoint, beauPapa, belleMaman)
        self.Enfants.set(enfants)
        self.Fratrie.set(fratrie)
