from django.db import models

class  Destination(models.Model):
    img = models.ImageField(upload_to ='pics')
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    paragraph = models.TextField(max_length=100)
    offer = models.BooleanField(default=False)

class News(models.Model):
    
    img = models.ImageField(upload_to="pics")
    date = models.IntegerField()
    month = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=43)
    paragraph = models.TextField(max_length=100)
    
