from django import forms

from .models import Cocktail, Ingredient

class IngredientForm(forms.ModelForm):
    
    class Meta:
        model = Ingredient
        fields = ('name','type','desc')
        
class CocktailForm(forms.ModelForm):
    
    class Meta:
        model = Cocktail
        fields = ('name','ingredients','directions','desc')