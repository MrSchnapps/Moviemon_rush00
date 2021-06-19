from django.shortcuts import render
from random import *
from django.conf import settings
from .Game import *
from django.views.generic import TemplateView
# Create your views here.

def loadMap() :
    #map = [40][40]
    #for row in map :
      #  for case in row :
    game = Game()

    with open("moviemon/save1_example", 'r') as file :
        infos = file.read()
    game.load(infos)


class MapPageView(TemplateView):
	template_name = 'map.html'

def index(request):
    loadMap()
    return render(request, 'index.html')