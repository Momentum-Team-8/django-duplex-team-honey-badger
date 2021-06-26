from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, Card, User
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, "flashcards/homepage.html")

@login_required
def profile_page(request):
    return render(request, "flashcards/profile_page.html")