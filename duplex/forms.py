from django.forms import ModelForm
# from django.db import models
# from django.db.models import fields
from .models import Album


class AlbumForm(ModelForm):
    
    class Meta:
        model = Album
        fields = [
            'title',
            'artist',
            'cover_art',
        ]