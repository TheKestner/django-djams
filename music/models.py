from django.db import models

# Create your models here.

class Song(models.Model):
    song_name = models.CharField(max_length=500)

class Artist(models.Model):
    artist_name = models.CharField(max_length=500)

class Album(models.Model):
    song = models.ManyToManyField(Song)
    artist = models.ManyToManyField(Artist)
    album_name = models.CharField(max_length=500)