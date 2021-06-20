from django.shortcuts import render
from random import *
from django.conf import settings
from .Game import *
from django.views.generic import TemplateView
from . import generate_map as g_map
from . import imdb_scraper as scr
from time import sleep
from django.http import HttpResponseRedirect
# Create your views here.

def loadMap() :
    
    game = Game()
    game.load_default_settings()
    # loadsettings to load the correct info
    file_content = g_map.get_file_content()
    pos = g_map.get_pos(file_content)
    g_map.generate_map(pos[0], pos[1], settings.ROWS, settings.COLUMNS)  # changer le hardcode
    with open("moviemon/save1_example", 'r') as file :
        infos = file.read()
    # game.load(infos)

class MapPageView(TemplateView):
	template_name = 'map.html'

def index(request):
    loadMap()
    return render(request, 'index.html')

def moveup(request):
    g_map.move_character_up()
    return HttpResponseRedirect('/worldmap/')

def movedown(request):
    g_map.move_character_down()
    return HttpResponseRedirect('/worldmap/')

def moveleft(request):
    g_map.move_character_left()
    return HttpResponseRedirect('/worldmap/')

def moveright(request):
    g_map.move_character_right()
    return HttpResponseRedirect('/worldmap/')
