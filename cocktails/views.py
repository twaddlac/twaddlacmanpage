from django.shortcuts import render
from .models import Cocktail
from .forms import IngredientForm, CocktailForm

# Create your views here.
def cocktail_list(request):
    #cocktails = Cocktail.objects.filter(ingredients="bourbon")
    cocktails = Cocktail.objects.all()
    return render(request, 'cocktails/cocktail_list.html', {'cocktails':cocktails})
    
def new_cocktail(request):
    form = CocktailForm()
    return redner(request, 'cocktail/cocktail_edit.html', {'form': form})
    
def new_ingredient(request):
    form = IngredientForm()
    return redner(request, 'cocktail/ingredient_edit.html', {'form': form})