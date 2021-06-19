from django.shortcuts import render
from random import *
from django.conf import settings
from .Game import *
from django.views.generic import TemplateView
from . import generate_map as g_map
from time import sleep
from django.http import HttpResponseRedirect
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

def moveup(request):
    file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'r')
    file_content = file.readlines()
    pos = file_content[0].split(',')
    g_map.generate_map(int(pos[0]), int(pos[1]) + 1, 7, 7)
    # g_map.generate_map(0, 0 + 1, 7, 7)
    file_content[0] = file_content[0].replace(pos[1], str(int(pos[1]) + 1)) + '\n'
    file.close()
    file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
    for elem in file_content:
        file.write('{}'.format(elem))
    file.close()
    return HttpResponseRedirect('/worldmap/')
# def movedown(request):

# def moveleft(request):

# def moveright(request):