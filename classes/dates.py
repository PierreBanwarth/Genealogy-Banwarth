import datetime # we will use this for date objects
import json
from  classes.fichiers import *
from classes.utils import *

class Date:
    def __init__(self, json):
        if 'Approximative' in json['key']:
            self.exact = False
        else:
            self.exact = True
        self.date = json['value']
        if 'vers' in self.date:
            self.exact = False
        if 'avant' in self.date:
            self.exact = False
        if 'apres' in self.date:
            self.exact = False
        if 'ou' in self.date:
            self.exact = False



    def __str__(self):
        if self.date == None:
            return ''
        else:
            return self.date

    def getAnnee(self):
        if self.exact:
            if len(self.date.split('/')) == 3 and isYear(self.date.split('/')[2]):
                return self.date.split('/')[2]
        elif len(self.date) == 4 and isYear(self.date):
            return self.date
        else:
            return None
