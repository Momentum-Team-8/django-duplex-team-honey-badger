from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck, Card, User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import DeckForm
# Create your views here.
def homepage(request):
    return render(request, "flashcards/homepage.html")

@login_required
def profile_page(request):
    return render(request, "flashcards/profile_page.html")

@login_required
def list_deck(request):
    decks = Deck.objects.all()
    return render(request, "flashcards/list_deck.html",
                  {"decks": decks})

@login_required
def add_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.created_date = timezone.now()
            deck.save()
            return redirect('list_deck')
    else:
        form = DeckForm()
    return render(request, 'flashcards/add_deck.html', {'form': form})

@login_required
def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.created_date = timezone.now()
            deck.save()
            return redirect('list_deck')
    else:
        form = DeckForm()
    return render(request, 'flashcards/add_deck.html', {'form': form})

@login_required
def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    deck.delete()
    return redirect('list_deck')