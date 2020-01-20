from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('pokemon/<int:pk>/', views.pokemon_detail, name='pokemon_detail'),
    path('pokemon/new/', views.pokemon_new, name='pokemon_new'),
    path('pokemon/<int:pk>/edit/', views.pokemon_edit, name='pokemon_edit'),
]