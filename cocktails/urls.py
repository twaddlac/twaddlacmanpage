from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cocktail_list, name='cocktail_list'),
]