from django import forms
from .models import Card, Deck


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = [
            'title',
        ]


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = [
            'front_prompt',
            'back_answer',
            'deck',
        ]
