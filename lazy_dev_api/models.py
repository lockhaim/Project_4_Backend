from django.contrib.postgres.fields import ArrayField
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    online = models.BooleanField()

class Guide(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    author_id = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    likes = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=1024, blank=True, null=True)
    image = models.CharField(max_length=1024, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    imageFile = models.ImageField(upload_to='images', blank=True, null=True)

