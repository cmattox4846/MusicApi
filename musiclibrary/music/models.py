from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    genre = models.CharField(max_length=50, null=True)
    likes = models.IntegerField()
