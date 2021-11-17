from django.db import models

# Create your models here.
class Guide(models.Model):
    name = models.CharField(max_length=32)
    author_id = models.IntegerField()
    likes = models.IntegerField()
    content = models.CharField(max_length=1024)
    image = models.CharField(max_length=128)
    rating = models.IntegerField()

class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=128)
    online = models.BooleanField()
