import random
from config import * 

class apple():
    def __init__(self):
        self.setNewLocation()

    def setNewLocation(self):
        self.x= random.randint(0,config.CELLWIDTH -1)
        self.y= random.randint(0,config.CELLHEIGHT -1)