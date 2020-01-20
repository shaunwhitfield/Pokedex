from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Pokemon
from .forms import PokemonForm

def pokemon_list(request):
    pokemons = Pokemon.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'dex/pokemon_list.html', {'pokemons': pokemons})

def pokemon_detail(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'dex/pokemon_detail.html', {'pokemon': pokemon})

def pokemon_new(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.author = request.user
            pokemon.published_date = timezone.now()
            pokemon.save()
            return redirect('pokemon_detail', pk=pokemon.pk)
    else:
        form = PokemonForm()
    return render(request, 'dex/pokemon_edit.html', {'form': form})

def pokemon_edit(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    if request.method == "POST":
        form = PokemonForm(request.POST, instance=pokemon)
        if form.is_valid():
            pokemon = form.save(commit=False)
            pokemon.author = request.user
            pokemon.published_date = timezone.now()
            pokemon.save()
            return redirect('pokemon_detail', pk=pokemon.pk)
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'dex/pokemon_edit.html', {'form': form})