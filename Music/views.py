from django.forms.forms import Form
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

# imported our models
from . models import Song, User, Playlist
from .forms import RegisterForm, LoginForm, PlaylistForm
from rest_framework.decorators import api_view
from .decorators import user_login_required


import os
import sklearn
import numpy as np
import pandas as pd
import joblib as joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from pandas import read_csv
import numpy as np
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import joblib as joblib
from joblib import dump, load
import argparse
import os
import matplotlib.pyplot as plt
import io
import urllib
import base64


@user_login_required
def index(request):
    user = get_user(request)
    global UserID
    UserID = request.session['user_id']
    songs = Song.objects.all()
    playlists = Playlist.objects.filter(User=request.session['user_id'])
    for x in songs:
        print(x.Audio)
    context = {"songs": songs, 'user': user, 'playlist': playlists}
    return render(request, "index.html", context)


def USERID():
    return UserID


def register(request):
    form = RegisterForm()
    success = None
    if request.method == 'POST':
        if User.objects.filter(Username=request.POST['Username']).exists():
            error = "This username is already taken"
            return render(request, 'Music/register.html', {'form': form, 'error': error})
        if User.objects.filter(Email=request.POST['Email']).exists():
            error = "This email is already taken"
            return render(request, 'Music/register.html', {'form': form, 'error': error})
        form = RegisterForm(request.POST)
        new_user = form.save(commit=False)
        new_user.save()
        success = "New User Created Successfully !"
    return render(request, 'register.html', {'form': form, 'success': success})


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        Username = request.POST['Username']
        Password = request.POST['Password']
        if User.objects.filter(Username=Username, Password=Password).exists():
            user = User.objects.get(Username=Username)
            # This is a session variable and will remain existing as long as you don't delete this manually or clear your browser cache
            request.session['user_id'] = user.id
            Userage = User.objects.get(id=request.session['user_id'])
            age = Userage.Age
            gender = Userage.Gender

            gender = gender.lower()

            if gender == 'male':
                gender = 1
            else:
                gender = 0

            model = os.path.join(
                "C:/Users/harman/MusicFinaltesting1/JupyterNotebook", "forest.pkl")
            model = joblib.load(model)
            data = [age, gender]
            x = np.array(data).reshape(1, -1)
            x = np.array(x, dtype=np.int64)

            results = model.predict(x)
            if results[0] == 0:
                results = 'HipHop'
            elif results[0] == 1:
                results = 'Jazz'
            elif results[0] == 2:
                results = 'Classical'
            elif results[0] == 3:
                results = 'Dance'
            elif results[0] == 4:
                results = 'Acoustic'
            print(results)
            request.session['RGenre'] = results
            return redirect('Music:index')
    return render(request, 'login.html', {'form': form})


def recommended_song(request):
    Songs = Song.objects.filter(Genre=request.session['RGenre'])
    user = get_user(request)
    playlists = Playlist.objects.filter(User=request.session['user_id'])
    context = {'user': user, 'songs': Songs, 'playlist': playlists}
    return render(request, 'recommendedsongs.html', context)


def get_user(request):
    return User.objects.get(id=request.session['user_id'])

    # do something with your results


@user_login_required
def playlist_view(request):
    context = {}
    form = PlaylistForm(request.POST)
    user = get_user(request)
    playlists = Playlist.objects.filter(User=request.session['user_id'])
    context = {'form': form, 'user': user, 'playlist': playlists}
    if request.method == 'POST':
        if form.is_valid():
            temp = form.cleaned_data.get("Songs")
            print(temp)
            form = PlaylistForm(request.POST)
            new_playlist = form.save(commit=False)
            new_playlist.save()
        else:
            print('nnooooooooooooooooooooooooooooooooo')
    return render(request, "createplaylist.html", context)


@api_view(['GET'])
def playlist_detail(request, id):

    if request.method == 'GET':
        singleplaylist = Playlist.objects.get(id=id)
        Playlistsongs = []
        for x in singleplaylist.Songs:
            Playlistsongs.append(Song.objects.get(id=x))
        user = get_user(request)
        songs = Playlistsongs
        playlists = Playlist.objects.filter(User=request.session['user_id'])
        context = {'singleplaylist': singleplaylist,
                   'user': user, 'songs': songs, 'playlist': playlists}

    return render(request, "singleplaylist.html", context)


@api_view(['DELETE'])
def delete_playlist(request, id):
    print(id)
    singleplaylist = Playlist.objects.get(id=id)
    print(singleplaylist.id)
    if request.method == 'DELETE':
        singleplaylist.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'})


def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('Music:login')


def chart_view(request):
    plt.plot(range(19))
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64decode(buf.read())
    uri = urllib.parse.quote(string)
    return render(request, 'home.html', {'data': uri})
