from django import urls
from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views 

urlpatterns = [
    path('', views.homepage, name="home"),
    path('accounts/', include('registration.backends.default.urls')),
    path('profile/', views.profile_page, name='profile_page'),
]