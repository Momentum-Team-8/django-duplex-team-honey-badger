
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
    path('decklist/<int:pk>/list_card', views.list_card, name='list_card'),
    path('decklist/<int:pk>/list_card/add_card', views.add_card, name='add_card'),
    path('decklist/<int:pk>/list_card/<int:pk>/edit_card', views.edit_card, name='edit_card'),
    path('decklist/<int:pk>/list_card/<int:pk>/delete_card', views.delete_card, name='delete_card'),

]