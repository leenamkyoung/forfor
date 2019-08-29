from django.db import models

class Twenty(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200) #현장 소개하는 글
    body = models.TextField() # 장소, 아파트 

    def __str__(self):
        return self.title

class Thirty(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200) #현장 소개하는 글
    body = models.TextField() # 장소, 아파트 

    def __str__(self):
        return self.title

class Forty(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=200) #현장 소개하는 글
    body = models.TextField() # 장소, 아파트 

    def __str__(self):
        return self.title

