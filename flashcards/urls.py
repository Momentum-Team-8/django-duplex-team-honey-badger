from django import urls
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.homepage, name="home"),
    path('accounts/', include('registration.backends.default.urls')),
    path('profile/', views.profile_page, name='profile_page'),
    path('decklist/', views.list_deck, name='list_deck'),
    path('decklist/add/', views.add_deck, name='add_deck'),
    path('decklist/<int:pk>/edit/', views.edit_deck, name='edit_deck'),
    path('decklist/<int:pk>/delete/', views.delete_deck, name='delete_deck'),
]