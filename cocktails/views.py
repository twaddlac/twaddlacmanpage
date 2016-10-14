from django.shortcuts import render
from .models import Cocktail

# Create your views here.
def cocktail_list(request):
    cocktails = Cocktail.objects.filter(ingredients="bourbon")
    return render(request, 'cocktails/cocktail_list.html', {'cocktails':cocktails})