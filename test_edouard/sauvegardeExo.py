from xml.dom import minidom
import xml.etree.ElementTree as ET
import collections
import os

#  Pour lancer le programme python test_edouard/mon_programme.py
#  Ou Fleche du haut puis Enter

# Ces commandes permettent d'ouvrir le fichier table1.xml
arbre = ET.parse('''C:\\Users\\ebanw\\Documents\\GitHub\\Genealogy-Banwarth\\data\\Table1.xml''') 
racine = arbre.getroot()

print('Premier programme avec Edouard')

# On initialise un tableau vide
tableauPersonne = {}
def cleanString(s):
    return str(s).encode('latin-1', 'replace').decode('latin-1')

for element in racine:
    objet = {}

    for sousElement in element:
        # On crée des variables nom et prénom
        # sousElement.tag => nom du champs
        # sousElement.text => valeur du champs
        # Not in => n'est pas dans le tableau
        # si nom du champs est == a "Nom"
        if sousElement.tag == "Prenom" and sousElement.text != None:
            objet['prenom'] = cleanString(sousElement.text)
        # idem avec prenom
        if sousElement.tag == "Nom" and sousElement.text != None:
            objet['nom'] = cleanString(sousElement.text)
        
        if sousElement.tag == "Enregist" and sousElement.text != None:
            objet['enregistrement'] = cleanString(sousElement.text)

        if sousElement.tag == "Br" and sousElement.text != None:
            objet['branche'] = cleanString(sousElement.text)

        if sousElement.tag == "Sosa" and sousElement.text != None:
            objet['sosa'] = cleanString(sousElement.text)

        if sousElement.tag == "LieuNaissance" and sousElement.text != None:
            objet['lieuNaissance'] = cleanString(sousElement.text)

        if sousElement.tag == "DNaissance" and sousElement.text != None:
            objet['dateDeNaissance'] = cleanString(sousElement.text)

        if sousElement.tag == "LieuMariage" and sousElement.text != None:
            objet['lieuMariage'] = cleanString(sousElement.text)

        if sousElement.tag == "DMariage" and sousElement.text != None:
            objet['dateDeMariage'] = cleanString(sousElement.text)

        if sousElement.tag == "Conj" and sousElement.text != None:
            objet['conjoint'] = cleanString(sousElement.text)

        if sousElement.tag == "Enfants" and sousElement.text != None:
            objet['enfants'] = cleanString(sousElement.text)

        if sousElement.tag == "Aine" and sousElement.text != None:
            objet['aine'] = cleanString(sousElement.text)

        if sousElement.tag == "Cadet" and sousElement.text != None:
            objet['cadet'] = cleanString(sousElement.text)

        if sousElement.tag == "LieuDeces" and sousElement.text != None:
            objet['lieuDeces'] = cleanString(sousElement.text)

        if sousElement.tag == "DDeces" and sousElement.text != None:
            objet['dateDeDeces'] = cleanString(sousElement.text)

        if sousElement.tag == "Profession" and sousElement.text != None:
            objet['profession'] = cleanString(sousElement.text)

        if sousElement.tag == "Conjoint2" and sousElement.text != None:
            objet['conjoint2'] = cleanString(sousElement.text)
            
        if sousElement.tag == "AdD" and sousElement.text != None:
            objet['ageDonneDeces'] = cleanString(sousElement.text)

        if sousElement.tag == "Note" and sousElement.text != None:
            objet['note'] = cleanString(sousElement.text)

        if sousElement.tag == "Rel" and sousElement.text != None:
            objet['religion'] = cleanString(sousElement.text)

        if sousElement.tag == "PMM" and sousElement.text != None:
            objet['merePresentMariage'] = cleanString(sousElement.text)

        if sousElement.tag == "PPM" and sousElement.text != None:
            objet['perePresentMariage'] = cleanString(sousElement.text)

        if sousElement.tag == "CdD" and sousElement.text != None:
            objet['CdD'] = cleanString(sousElement.text)

        if sousElement.tag == "RechEnf" and sousElement.text != None:
            objet['rechEnfantTermine'] = cleanString(sousElement.text)


    
    tableauPersonne[int(objet['sosa'])]  = objet

# "34" => int("34") => 34
# String               Entier (calculable +-*/)  
arbre = collections.OrderedDict(sorted(tableauPersonne.items()))




# Jouer avec Arbre
i = 30
pageHauteur = 20

