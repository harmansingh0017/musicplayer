from django.db.models.deletion import CASCADE
from djongo import models
from django import forms


class User(models.Model):
    OPTIONS = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    Firstname = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Username = models.CharField(max_length=255)
    Email = models.EmailField()
    Password = models.CharField(max_length=255)
    Gender = models.CharField(default='', max_length=255, choices=OPTIONS)
    Age = models.IntegerField()


class Song(models.Model):
    OPTIONS = (
        ('HipHop', 'HipHop'),
        ('Jazz', 'Jazz'),
        ('Classical', 'Classical'),
        ('Dance', 'Dance'),
        ('Acoustic', 'Acoustic')
    )
    Audio = models.CharField(max_length=255)
    Artist = models.CharField(max_length=255)
    Audiofile = models.FileField(blank=True, null=True)
    Imageurl = models.FileField(blank=True, null=True)
    Genre = models.CharField(max_length=100, choices=OPTIONS)
    Time = models.CharField(max_length=60)
    color = models.CharField(max_length=60, null=True)


class Playlist(models.Model):
    Playlistname = models.CharField(max_length=255)
    Songs = models.JSONField(models.CharField(max_length=255))
    User = models.IntegerField(null=True)
