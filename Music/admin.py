from django.contrib import admin

# Register your models here.
from . models import Playlist, User, Song

admin.site.register([Playlist, User, Song])
