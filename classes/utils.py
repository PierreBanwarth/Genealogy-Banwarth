def trouveNom(s):
    return s.isupper() and len(s)>2
def formatShortDate(s):
    jour = ''
    mois = ''
    tab = s.split('/')
    if len(tab) !=3:
        return s
    else:

        if len(tab[0]) == 1:
            jour = '0'+tab[0]
        elif len(tab[0]) == 0:
            jour = '??'
        else:
            jour = tab[0]
        if len(tab[1]) == 1:
            mois = '0'+tab[1]
        else:
            mois = tab[1]
        return jour+'/'+mois+'/'+tab[2]
def goodFormatDate(s):
    return len(s.split('/')) == 3  and len(s.split('/')[0]) == 2 and len(s.split('/')[1]) == 2 and len(s.split('/')[2]) == 4
def goodFormatDateApproximative(s):
    return len(s.split('/')) == 2  and len(s.split('/')[0]) == 4 and len(s.split('/')[1]) == 4
def trouveDate(s):
    return any(i.isdigit() for i in s)
def isYear(s):
    return all(i.isdigit() for i in s)
def formatDate(s):
    #"dateNaissance": "1833-05-21T00:00:00",
    if len(s) == len('1833-05-21T00:00:00'):
        array = s.split('T')[0].split('-')
        return array[2]+'/'+array[1]+'/'+array[0]
def dateEnfantFormat(s):
    array = s.split('/')
    result = ''
    if len(array) == 3:
        if len(array[0]) == 1:
            array[0] = '0'+array[0]
        elif len(array[0]) == 0:
            array[0] = '??'
        if len(array[1]) == 1:
            array[1] = '0'+array[1]
        return array[0]+'/'+array[1]+'/'+array[2]
    else:
        return s
def getLieuxFromString(s):
    if '*' in s:
        s = s.split('*')
        return {
            'departement' : s[0],
            'ville' : s[1]
        }

    else:
        s = s[1:]
        s = s.split(')')
        if s[0] == 'I':
            pays  ='Italie'
        if s[0] == 'D' or s[0] == 'B':
            pays  ='Swisse'
        if s[0] == 'S':
            pays  ='Allemagne'
        return {
            'pays' : pays,
            'ville' : s[1]
        }

def getInfosDecesMariage(tableauString, key, str):
    resultat = None
    if str in tableauString:
        indexChar = tableauString.index(str)
        index = indexChar+1

        if index < len(tableauString):
            resultat = tableauString[index]
            resultat = formatShortDate(resultat)
            if resultat == 'avant':
                resultat = tableauString[index+1]
                resultat = formatShortDate(resultat)
        if len(tableauString) > index:
            tableauString.pop(index)
        tableauString.remove(str)

    return {
        'tableauString' : tableauString,
        'resultat': {
            'key' : key,
            'value': resultat
        }
    }

def trouveDateKey(tableauString, objet, key):
    if 'vers' in tableauString:
        tableauString.remove('vers')
        prefix = 'vers '
    elif 'avant' in tableauString:
        tableauString.remove('avant')
        prefix = 'avant '
    elif 'apres' in tableauString:
        tableauString.remove('apres')
        prefix = 'apres '
    else:
        prefix = ''

    resultKey = key
    resultValue = None
    for s in tableauString:
        if trouveDate(s):
            dateClean = formatShortDate(s)
            resultValue = dateClean
            if goodFormatDate(dateClean) or isYear(dateClean):
                if prefix == 'vers ' or prefix == 'avant ' or prefix == 'apres ' or '?' in dateClean or len(dateClean) == 4:
                    resultKey = key+'Approximative'
                    resultValue = prefix+dateClean
            elif goodFormatDateApproximative(dateClean):
                resultKey = key+'Approximative'
                resultValue = dateClean.split('/')[0] +' ou '+dateClean.split('/')[1]

            tableauString.remove(s)
    return {
        'tableauString' : tableauString,
        'resultat': {
            'key' : resultKey,
            'value': resultValue
        }
    }
def cleanString(s):
    result = s.split(' ')
    while '' in  result:
        result.remove('')

    for i in range(len(result)):
        onlyX = True
        if 'X' in result[i]:
            for x in result[i]:
                if x != 'X':
                    onlyX = False
        if onlyX:
            result[i] = result[i].lower()
    return result
