import datetime # we will use this for date objects
from tkinter import *
from personne import Personne


class PersonneLabel:
    def __init__(self, personne, labelPere):
        self.textNom = StringVar()
        self.textDateNaissance = StringVar()
        self.textLieuNaissance = StringVar()
        self.textDeces =StringVar()
        self.textLieuDeces =StringVar()
        self.textAge = StringVar()
        self.textProfession = StringVar()

        self.labelNom = Label(labelPere, textvariable=self.textNom)
        self.labelNaissance = Label(labelPere, textvariable=self.textDateNaissance)
        self.labelLieuNaissance = Label(labelPere, textvariable=self.textLieuNaissance)
        self.labelDeces = Label(labelPere, textvariable=self.textDeces)
        self.labelLieuDeces = Label(labelPere, textvariable=self.textLieuDeces)
        self.labelAge = Label(labelPere, textvariable=self.textDateNaissance)
        self.labelProfession = Label(labelPere, textvariable=self.textProfession)
        self.set(personne)
        
    def pack(self):
        self.labelNom.pack()
        self.labelNaissance.pack()
        self.labelLieuNaissance.pack()
        self.labelDeces.pack()
        self.labelLieuDeces.pack()
        self.labelAge.pack()
        self.labelProfession.pack()

    def set(self, personne):
        self.textNom.set('Nom :'+personne.Nom +' '+personne.Prenom)
        self.textDateNaissance.set('Date de Naissance :'+personne.DateNaissance)
        self.textLieuNaissance.set('Lieu de Naissance :'+personne.getLieuNaissance())
        self.textDeces.set('Date de deces :'+personne.DateDeces)
        self.textLieuDeces.set('Lieu de deces :'+personne.getLieuDeces())
        self.textAge.set('Age :'+personne.getAge())
        self.textProfession.set('Profession'+personne.Profession)
