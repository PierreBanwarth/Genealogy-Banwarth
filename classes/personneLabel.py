import datetime # we will use this for date objects
from tkinter import *
from classes.personne import Personne

from PIL import Image, ImageTk

class ParentLabel():
    def __init__(self, personne, labelPere):
        self.textNom = StringVar()
        self.textDateNaissance = StringVar()
        self.textLieuNaissance = StringVar()
        self.textDeces =StringVar()
        self.textLieuDeces =StringVar()
        self.textAge = StringVar()
        self.textProfession = StringVar()

        self.labelNom = Label(labelPere, textvariable=self.textNom, bg='white')
        self.labelNaissance = Label(labelPere, textvariable=self.textDateNaissance, bg='white')
        self.labelLieuNaissance = Label(labelPere, textvariable=self.textLieuNaissance, bg='white')
        self.labelDeces = Label(labelPere, textvariable=self.textDeces, bg='white')
        self.labelLieuDeces = Label(labelPere, textvariable=self.textLieuDeces, bg='white')
        self.labelAge = Label(labelPere, textvariable=self.textDateNaissance, bg='white')
        self.labelProfession = Label(labelPere, textvariable=self.textProfession, bg='white')
        self.set(personne, labelPere)

    def pack(self):
        self.labelNom.pack()
        self.labelNaissance.pack()
        self.labelLieuNaissance.pack()
        self.labelDeces.pack()
        self.labelLieuDeces.pack()
        self.labelAge.pack()
        self.labelProfession.pack()
        self.labelProfession.pack()
        self.labelProfession.pack()
    def destroy(self):
        self.labelNom.destroy()
        self.labelNaissance.destroy()
        self.labelLieuNaissance.destroy()
        self.labelDeces.destroy()
        self.labelLieuDeces.destroy()
        self.labelAge.destroy()
        self.labelProfession.destroy()
        self.labelProfession.destroy()
        self.labelProfession.destroy()

    def set(self, personne, labelPersonne):
        self.textNom.set('Nom :'+personne.Nom +' '+personne.Prenom)
        self.textDateNaissance.set('Date de Naissance : '+str(personne.DateNaissance))
        if personne.LieuNaissance != None:
            self.textLieuNaissance.set('Lieu de Naissance : '+personne.LieuNaissance)
        self.textDeces.set('Date de deces : '+str(personne.DateDeces))
        if personne.LieuDeces != None:
            self.textLieuDeces.set('Lieu de deces : '+personne.LieuDeces)
        if personne.Profession != None:
            self.textAge.set('Age : '+personne.getAge())
        if personne.Profession != None:
            self.textProfession.set('Profession : '+personne.Profession)
        self.pack()


class EnfantLabel():

    def __init__(self, enfant, labelEnfant):
        self.textNom = StringVar()
        self.textDateNaissance = StringVar()
        self.textDateDeces =StringVar()
        self.textDateMariage =StringVar()
        self.textSosa =StringVar()

        self.labelNom = Label(labelEnfant, textvariable=self.textNom, bg='white')
        self.labelDateNaissance = Label(labelEnfant, textvariable=self.textDateNaissance, bg='white')
        self.labelDateDeces = Label(labelEnfant, textvariable=self.textDateDeces, bg='white')
        self.labelDateMariage = Label(labelEnfant, textvariable=self.textDateMariage, bg='white')
        self.labelLieuDeces = Label(labelEnfant, textvariable=self.textSosa, bg='white')
        self.set(labelEnfant, enfant)

    def set(self, labelEnfant, enfant):
        if enfant.Prenom != None:
            self.textNom.set(enfant.Prenom)

        if enfant.DateNaissance != None:
            self.textDateNaissance.set(enfant.DateNaissance)

        if enfant.DateMariage != None:
            self.textDateMariage.set(enfant.DateMariage)

        if enfant.DateDeces != None:
            self.textDateDeces.set(enfant.DateDeces)

        if enfant.Sosa != None:
            self.textSosa.set(enfant.Sosa)

    def pack(self):
        self.labelNom.pack()
        self.labelDateNaissance.pack()
        self.labelDateDeces.pack()
        self.labelDateMariage.pack()
        self.labelLieuDeces.pack()

    def destroy(self):
        self.labelNom.destroy()
        self.labelDateNaissance.destroy()
        self.labelDateDeces.destroy()
        self.labelDateMariage.destroy()
        self.labelLieuDeces.destroy()


class PersonneLabel():
    def __init__(self, personne, labelPersonne, labelEnfant, labelPere, labelMere, arbre):
        self.Pere = None
        self.Mere = None
        self.Personne = None
        self.Enfants = None

        self.labelPersonne = labelPersonne
        self.labelPere = labelPere
        self.labelMere = labelMere
        self.labelEnfant = labelEnfant

        self.enfantsLabel = []

        self.set(personne, labelPersonne, arbre)


    def pack(self):
        self.Personne.pack()
        self.Pere.pack()
        self.Mere.pack()
        for item in self.enfantsLabel:
            item.pack()



    def set(self, personne, labelPersonne, arbre):
        personnePere = arbre[personne.getPere()]
        personneMere = arbre[personne.getMere()]
        enfants = personne.getEnfants()
        if self.Pere != None:
            self.Pere.destroy()

        if self.Pere != None:
            self.Mere.destroy()

        if self.Personne != None:
            self.Personne.destroy()

        if len(self.enfantsLabel)>0:
            for item in self.enfantsLabel:
                item.destroy()

        self.Pere = ParentLabel(personnePere, self.labelPere)
        self.Mere = ParentLabel(personneMere, self.labelMere)
        self.Personne = ParentLabel(personne, self.labelPersonne)
        self.enfantsLabel = []
        if len(enfants)>0:
            for item in  enfants:
                enfant = EnfantLabel(item,  self.labelEnfant)
                self.enfantsLabel.append(enfant)
                enfant.pack()
        self.pack()
