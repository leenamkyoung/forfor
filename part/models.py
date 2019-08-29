from django.db import models

class Bed(models.Model):
    image = models.ImageField(upload_to='images/')

class Bath(models.Model):
    image = models.ImageField(upload_to='images/')

class Door(models.Model):
    image = models.ImageField(upload_to='images/')

class Dressroom(models.Model):
    image = models.ImageField(upload_to='images/')

class Kitchen(models.Model):
    image = models.ImageField(upload_to='images/')
    

class Livingroom(models.Model):
    image = models.ImageField(upload_to='images/')

class Veranda(models.Model):
    image = models.ImageField(upload_to='images/')