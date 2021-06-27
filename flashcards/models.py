from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"

    def __str__(self):
        return self.username


class Deck(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    
    def __repr__(self):
        return f"<Deck title={self.title}>"

    def __str__(self):
        return self.title

class Card(models.Model):
    front_prompt = models.CharField(max_length=600)
    back_answer = models.CharField(max_length=900)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="cards")

    def __repr__(self):
        return f"<Card prompt={self.front_prompt}>"

    def __str__(self):
        return self.front_prompt