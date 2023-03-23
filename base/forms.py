from django.forms import ModelForm
from . models import Song, User

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'
        exclude = ['creator', 'contributors', 'favorite', 'album_art']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email']