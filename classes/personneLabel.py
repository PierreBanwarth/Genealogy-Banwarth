import datetime # we will use this for date objects
from tkinter import *
from classes.personne import Personne


class PersonneLabel:
    def __init__(self, personne, labelPere, labelEnfant):
        self.labelPere  = labelPere
        self.labelEnfant  = labelEnfant

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
        self.enfantsLabel = []
        self.enfantsText = []

        for index, item in enumerate(personne.getEnfants()):
            self.enfantsText.append(StringVar())
            self.enfantsLabel.append(Label(self.labelEnfant, textvariable=self.enfantsText[index]))

        self.set(personne)


    def pack(self):
        self.labelNom.pack()
        self.labelNaissance.pack()
        self.labelLieuNaissance.pack()
        self.labelDeces.pack()
        self.labelLieuDeces.pack()
        self.labelAge.pack()
        self.labelProfession.pack()
        for item in self.enfantsLabel:
            item.pack()

    def set(self, personne):
        for item in self.enfantsLabel:
            item.destroy()

        self.enfantsLabel = []
        self.enfantsText = []

        for index, item in enumerate(personne.getEnfants()):
            self.enfantsText.append(StringVar())
            self.enfantsLabel.append(Label(self.labelEnfant, textvariable=self.enfantsText[index]))

        self.textNom.set('Nom :'+personne.Nom +' '+personne.Prenom)
        self.textDateNaissance.set('Date de Naissance :'+personne.DateNaissance)
        self.textLieuNaissance.set('Lieu de Naissance :'+personne.getLieuNaissance())
        self.textDeces.set('Date de deces :'+personne.DateDeces)
        self.textLieuDeces.set('Lieu de deces :'+personne.getLieuDeces())
        self.textAge.set('Age :'+personne.getAge())
        self.textProfession.set('Profession'+personne.Profession)

        for index, item in enumerate(personne.getEnfants()):
            if 'Prenom' in item:
                self.enfantsText[index].set(item['Prenom'])
            else:
                self.enfantsText[index].set(item['nom']+' '+item['prenom'])
        self.pack()
