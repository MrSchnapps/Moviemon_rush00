from django.shortcuts import render
from random import *
from django.conf import settings
from .Game import *
from django.views.generic import TemplateView
from time import sleep
from django.http import HttpResponseRedirect
from .moviedex import *
from . import generate_map as g_map
from . import imdb_scraper as scr
from battle import *
# Create your views here.

def loadMap() :
    
    game = Game()
    game.load_default_settings()
    # with open('moviemon/current_save.save') as file:
    #     game.load(file.read())
    # loadsettings to load the correct info
    # file_content = g_map.get_file_content()
    # pos = g_map.get_pos(file_content)
    g_map.generate_map(game.pos[0], game.pos[1], settings.ROWS, settings.COLUMNS, 0, game)
    game.write_infos()
    list_of_moviemons = scr.load_all_moviemons()
    for moviemon in list_of_moviemons:

    # with open("moviemon/save1_example", 'r') as file :
    #     infos = file.read()
    # game.load(infos)

class MapPageView(TemplateView):
	template_name = 'map.html'

### main page
def index(request):
    loadMap()
    return render(request, 'index.html')

### movement
def moveup(request):
    g_map.move_character('up')
    return HttpResponseRedirect('/worldmap/')

def movedown(request):
    g_map.move_character('down')
    return HttpResponseRedirect('/worldmap/')

def moveleft(request):
    g_map.move_character('left')
    return HttpResponseRedirect('/worldmap/')

def moveright(request):
    g_map.move_character('right')
    return HttpResponseRedirect('/worldmap/')

### moviedex
def moviedex(request) :
    generate_moviedex()
    return (render, 'moviedex.html')

### battle
def gladiator(request):
    

def throw_ball(request):