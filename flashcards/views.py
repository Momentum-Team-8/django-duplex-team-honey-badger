from django.db.models.fields import BooleanField
from flashcards.forms import CardForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Deck, Card, User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import DeckForm
from django.http import JsonResponse
# Create your views here.
def homepage(request):
    return render(request, "flashcards/homepage.html")

@login_required
def profile_page(request):
    return render(request, "flashcards/profile_page.html")

@login_required
def list_deck(request):
    decks = Deck.objects.all()
    return render(request, "flashcards/list_deck.html", {"decks": decks})


def list_card(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = deck.cards.filter(marked_as_right=False).order_by('?')
    return render(request, "flashcards/list_card.html", {"cards": cards, "deck": deck, "pk": pk})


def add_card(request, pk):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.created_date = timezone.now()
            card.save()
            return redirect('list_card', pk=pk)
    else:
        form = CardForm()
    return render(request, 'flashcards/add_card.html', {'form': form})


def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            card = form.save(commit=False)
            card.created_date = timezone.now()
            card.save()
            return redirect('list_card', pk=card.deck_id)
    else:
        form = CardForm()
    return render(request, 'flashcards/edit_card.html', {'form': form, 'card': card})


def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.delete()
    return redirect('list_card', pk=card.deck_id)


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


# def mark_correct(request, pk):
#     card = get_object_or_404(Card, pk=pk)
#     if marked_as_right.filter(id=card.id).exists():
#         correct = True
#     else:
#         correct = False
#     card.save()
    
#     if request.headers.get("x-requested-with") == "XMLHttpRequest":
#         return JsonResponse({"correct": correct}, status=200)


def mark_correct(request, pk):
    card = get_object_or_404(Card, pk=pk)
    card.marked_as_right = True
    card.save()

    return JsonResponse({"card.id": card.id}, status=200)

    