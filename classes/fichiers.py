
import json

try:
    to_unicode = unicode
except NameError:
    to_unicode = str



def getRegnes():
    with open('data/regnes.json') as json_file:
        regnes = json.load(json_file)
        return regnes

def getAstrologie():
    with open('data/astrologie.json') as json_file:
        astrologie = json.load(json_file)
        return astrologie



def getFichierRegions():
    with open('data/departements-region.json') as json_file:
        regions = json.load(json_file)
        return regions

def sauvegardeBase(jsonFinal, filename):
    with open(filename, 'w', encoding='utf8') as outfile:
        str_ = json.dumps(
            jsonFinal,
            indent=4, sort_keys=True,
            separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))

def sauvegardeBasePersonne(result, filename):
    finalJson = {}
    for sosa, personne in result.items():
        finalJson[sosa] = personne.toJSON()
    sauvegardeBase(finalJson,filename)

def openBase(filename):
    with open(filename) as json_file:
        return json.load(json_file)
