

def plotRepartitionAnnuelle(result):
    test = {}
    for k, v in result.items():
        year = v.getAnneeNaissance()
        if year != None:
            if year not in test:
                test[int(year)] = 1
            else:
                test[int(year)] = test[year]+1
        for item in v.getEnfants():
            if item.getDateNaissance() != None:
                year = item.getAnneeNaissance()
                if year != None:
                    if year not in test:
                        test[year] = 1
                    else:
                        test[year] = test[year]+1
    od = collections.OrderedDict(sorted(test.items()))
    names = []
    values = []

    for k, v in test.items():
        names.append(k)
