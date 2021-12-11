from django import forms
from django.db.models import fields
from django.forms import widgets
from django.http import request
from django.views.decorators.csrf import csrf_protect


from Music.views import User
from .models import Song, User, Playlist

passwordInputWidget = {
    'Password': forms.PasswordInput()
}


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = [passwordInputWidget]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['Username', 'Password']
        widgets = [passwordInputWidget]


song = Song.objects.all()
choice_f = []
for x in song:
    choice_f.append((x.id, x.Audio))
for i in choice_f:
    print(i)


Songswidget = {
    'Songs': forms.CheckboxSelectMultiple(choices=choice_f)

}


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['Playlistname', 'Songs', 'User']
        widgets = [Songswidget]

    Playlistname = forms.CharField()
    Songs = forms.MultipleChoiceField(
        choices=choice_f,
        widget=forms.CheckboxSelectMultiple
    )
    User = forms.IntegerField()
