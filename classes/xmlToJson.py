def convertXMLFile():
    arbre = ET.parse('data/table1.xml')
    racine = arbre.getroot()
    jsonBySosa = convertirBase(racine)
    result = retrouverEnfant(jsonBySosa)
    sauvegardeBasePersonne(jsonBySosa, 'data/baseDeDonneeBySosa.json')



lieux = []
def parseListeEnfants(s):
    listeEnfantFinale = []
    listeEnfants = s.split('\n')

    if '*' in listeEnfants:
        listeEnfants.remove('*')

    for enfantString in listeEnfants:
        enfant = enfantFromString(enfantString)
        listeEnfantFinale.append(enfant)
    return listeEnfantFinale




def parseConjoint(s):
    conjoint = {}
    infosConjoint = cleanString(s)
    TrouveDate = False
    resultat = getInfosDecesMariage(infosConjoint, 'dateDeces', '+')
    infosConjoint = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        conjoint['dateDeces'] = resultat['resultat']['value']

    resultat = getInfosDecesMariage(infosConjoint, 'dateNaissance', 'o')
    if resultat['resultat']['value'] != None:
        conjoint['dateNaissance'] = resultat['resultat']['value']

    resultat = trouveDateKey(infosConjoint, conjoint, 'DateMariage')
    infosEnfant = resultat['tableauString']
    if resultat['resultat']['value'] != None:
        conjoint['DateMariage'] = resultat['resultat']

    TrouveNom = False
    for item in infosConjoint:
        if(trouveNom(item)):
            if 'Nom' in conjoint:
                conjoint['Nom'] = conjoint['Nom']+' '+str(item)
            else:
                conjoint['Nom'] = str(item)
            infosConjoint.remove(item)
    # if 'Nom' in conjoint:
    #     print(conjoint['Nom'])
    if len(infosConjoint) == 1:
        conjoint['Prenom']  = ' '.join(infosConjoint)

    elif infosConjoint == ['xxx', 'xxxxx']:
        conjoint['Prenom'] = 'Inconnu'
        conjoint['Nom'] = 'Inconnu'
    elif 'x' in infosConjoint:
        infosConjoint.remove('x')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 1
    elif 'xx' in infosConjoint:
        infosConjoint.remove('xx')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 2
    elif 'xxx' in infosConjoint:
        infosConjoint.remove('xxx')
        conjoint['Prenom'] = ' '.join(infosConjoint)
        conjoint['NumeroMariage'] = 3

    elif(len(infosConjoint)==2):
        conjoint['Prenom'] = ' '.join(infosConjoint)
    else:
        conjoint['info'] = ' '.join(infosConjoint)
    # if 'Prenom' in conjoint:
    #     print(conjoint['Prenom'])

    return conjoint




def convertirBase(racine):
    listPersonne = {}


    erreursEnfants = []
    erreursConjoints = []

    for element in racine:
        personne = Personne()
        conjoints = []

        for sousElement in element:
            if sousElement != None and sousElement.text != None and sousElement.tag != None:
                if sousElement.tag == 'Prenom':
                    personne.setPrenom(sousElement.text)
                elif sousElement.tag == 'PPM':
                    personne.setPerePresentMariage(sousElement.text)
                elif sousElement.tag == 'PMM':
                    personne.setMerePresenteMariage(sousElement.text)
                elif sousElement.tag == 'DMariage':
                    personne.setDateMariage(formatDate(sousElement.text))
                elif sousElement.tag == 'DNaissance':
                    personne.setDateNaissance(formatDate(sousElement.text))
                elif sousElement.tag == 'DDeces':
                    personne.setDateDeces(formatDate(sousElement.text))
                elif sousElement.tag == 'Enregist':
                    personne.setEnregistrement(sousElement.text)
                elif sousElement.tag == 'Rel':
                    personne.setReligion(sousElement.text)
                elif sousElement.tag == 'AdD':
                    personne.setAgeDeces(sousElement.text)
                elif sousElement.tag == 'RechEnf':
                    personne.setRechercheEnfantTermine()
                elif sousElement.tag == 'CdD':
                    personne.setConjointDecedesDeces(sousElement.text)
                elif sousElement.tag == 'Profession':
                    if sousElement.text[0] == '-' or sousElement.text[0] == '+':
                        personne.setProfession(sousElement.text[1:])
                elif sousElement.tag == 'Nom':
                    personne.setNom(sousElement.text)
                elif sousElement.tag == 'Br':
                    personne.setBranche(sousElement.text)
                elif sousElement.tag == 'Sosa':
                    personne.setSosa(sousElement.text)
                elif sousElement.tag == 'Cadet':
                    personne.setCadet(sousElement.text)
                elif sousElement.tag == 'Note':
                    personne.setNote(sousElement.text)
                elif sousElement.tag == 'Aine':
                    personne.setAine(sousElement.text)

                elif sousElement.tag == 'LieuNaissance':
                    personne.setLieuNaissance(sousElement.text)
                elif sousElement.tag == 'LieuDeces':
                    personne.setLieuDeces(sousElement.text)
                elif sousElement.tag == 'LieuMariage':
                    personne.setLieuMariage(sousElement.text)


                elif sousElement.tag == 'Conj':
                    conjoint = parseConjoint(sousElement.text)
                    conjoints.append(conjoint)
                elif sousElement.tag == 'Conjoint2':
                    infosConjoint = sousElement.text.split('\n')
                    for item in infosConjoint:
                        conjoint = parseConjoint(item)
                        conjoints.append(conjoint)
                elif sousElement.tag == 'Enfants':
                    personne.setEnfants(parseListeEnfants(sousElement.text))
                    # print(personne.getEnfants())

        personne.setConjoint(conjoints)
        sosa = personne.getSosa()
        listPersonne[int(sosa)] = personne

    return listPersonne

def retrouverEnfant(jsonBySosa):
    result = {}
    for sosa, personne in jsonBySosa.items():
        sosaFils = personne.getSonSosa()
        if sosa != sosaFils:
            fils = Enfant()
            fils.setJson(jsonBySosa[sosaFils])

            personne.addAine(fils)
        result[sosa] = personne
    return result
