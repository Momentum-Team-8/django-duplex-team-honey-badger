from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, Card
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, "flashcards/homepage.html")