from django.conf import settings
from django.conf.urls import static, url
from django.urls import path, include
from . import views

app_name = "Music"

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('recommendedsong/', views.recommended_song, name='recommendedsong'),
    path(r'^singleplaylist/(?P<id>[0-9]+)$',
         views.playlist_detail, name='singleplaylist'),
     path('logout/', views.logout, name='logout')



]
