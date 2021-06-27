<<<<<<< HEAD
from django.forms import ModelForm
from .models import Card


class CardForm(ModelForm):
    
    class Meta:
        model = Card
        fields = [
            'front_prompt',
            'back_answer',
            'deck',
=======
from django import forms

from .models import Deck, Card

class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'title', 
>>>>>>> main
        ]