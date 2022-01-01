import datetime # we will use this for date objects
import json
from  classes.fichiers import *


class Date:
    def __init__(self, json):
        if 'Approximative' in json['key']:
            self.exact = False
        else:
            self.exact = True
        self.date = json['value']

    def __str__(self):
        if self.date == None:
            return ''
        else:
            return self.date
