from django.db import models

class Package (models.Model):
    name = models.CharField(max_length = 200)
    pol = models.CharField(max_lenght = 200) #posiçao atual
    pos = models.CharField(max_lenght = 200) #desitno

    def __init__(self, name,pol,pos):
        self.name =  name
        self.pol = pol
        self.pos = pos
    
    def getName()
        return self.name

    def getPol()
        return self.pol
    
    def getPos()
        return self.pos
    
