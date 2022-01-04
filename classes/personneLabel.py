import datetime # we will use this for date objects
from tkinter import *
from classes.personne import Personne

from PIL import Image, ImageTk

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

        self.labelNom = Label(labelPere, textvariable=self.textNom, bg='white')
        self.labelNaissance = Label(labelPere, textvariable=self.textDateNaissance, bg='white')
        self.labelLieuNaissance = Label(labelPere, textvariable=self.textLieuNaissance, bg='white')
        self.labelDeces = Label(labelPere, textvariable=self.textDeces, bg='white')
        self.labelLieuDeces = Label(labelPere, textvariable=self.textLieuDeces, bg='white')
        self.labelAge = Label(labelPere, textvariable=self.textDateNaissance, bg='white')
        self.labelProfession = Label(labelPere, textvariable=self.textProfession, bg='white')
        self.enfantsLabel = []
        self.enfantsText = []


        for index, item in enumerate(personne.getEnfants()):
            self.enfantsText.append(StringVar())
            self.enfantsLabel.append(Label(self.labelEnfant, textvariable=self.enfantsText[index]))

        self.set(personne, labelPere)


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



    def set(self, personne, labelPere):
        for item in self.enfantsLabel:
            item.destroy()
        self.enfantsLabel = []
        self.enfantsText = []

        for index, item in enumerate(personne.getEnfants()):
            self.enfantsText.append(StringVar())
            self.enfantsLabel.append(Label(self.labelEnfant, textvariable=self.enfantsText[index]))

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

        for index, item in enumerate(personne.getEnfants()):
            if personne.getPrenom() != None:
                self.enfantsText[index].set(personne.getPrenom())
            else:
                self.enfantsText[index].set(personne.getPrenom())
        self.pack()
