import datetime # we will use this for date objects
import json
from  classes.fichiers import *
from classes.utils import *

class Date:

    def __init__(self, json):
        self.exact = 'Approximative' not in json['key'] or 'vers' in self.date or  'avant' in self.date or 'apres' in self.date or 'ou' in self.date
        self.date = json['value']

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
