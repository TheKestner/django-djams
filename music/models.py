from django.db import models

# Create your models here.

class Song(models.Model):
    song_name = models.CharField(max_length=500)

    def __str__(self):
        return self.song_name

class Artist(models.Model):
    artist_name = models.CharField(max_length=500)

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    song = models.ManyToManyField(Song)
    artist = models.ManyToManyField(Artist)
    album_name = models.CharField(max_length=500)

    def __str__(self):
        return self.album_name