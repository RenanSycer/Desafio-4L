from django.db import models

class Package (models.Model):
    name = models.CharField(max_length = 200)
    pol = models.CharField(max_length = 200) #posiçao atual (país)
    pos = models.CharField(max_length = 200) #desitno (país)

    def __str__(self):
        return self.name 
    
    # def getName(self):
    #     return self.name

    # def getPol(self):
    #     return self.pol
    
    # def getPos(self):
    #     return self.pos
    
