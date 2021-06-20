from django.shortcuts import render
from random import *
from django.conf import settings
from .Game import Game
from django.views.generic import TemplateView
from time import sleep
from django.http import HttpResponseRedirect
# from .moviedex import *
from . import generate_map as g_map
from . import imdb_scraper as scr
from .battle import *
from .moviedex import *
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
	mvm_found = g_map.move_character('up')
	if (mvm_found == 0):
		return HttpResponseRedirect('/worldmap/')
	else:
		file = open('./moviemon/moviemon_fight', 'w')
		file.write('Gladiator')
		file.close()
		return (HttpResponseRedirect('/battle/Moviemon'))

def movedown(request):
	mvm_found = g_map.move_character('down')
	if (mvm_found == 0):
		return HttpResponseRedirect('/worldmap/')
	else:
		file = open('./moviemon/moviemon_fight', 'w')
		file.write('Gladiator')
		file.close()
		return (HttpResponseRedirect('/battle/Moviemon'))

def moveleft(request):
	mvm_found = g_map.move_character('left')
	if (mvm_found == 0):
		return HttpResponseRedirect('/worldmap/')
	else:
		file = open('./moviemon/moviemon_fight', 'w')
		file.write('Gladiator')
		file.close()
		game = Game.Game()
		generate_battle(game, game.get_random_movie())
		return (HttpResponseRedirect('/battle/Moviemon'))

def moveright(request):
	mvm_found = g_map.move_character('right')
	if (mvm_found == 0):
		return HttpResponseRedirect('/worldmap/')
	else:
		file = open('./moviemon/moviemon_fight', 'w')
		file.write('Gladiator')
		file.close()
		return (HttpResponseRedirect('/battle/Moviemon'))

### moviedex
# def moviedex(request) :
# 	generate_moviedex()
# 	return render(request, 'moviedex.html')

### moviedex
def moviedex(request) :
	dico = generate_moviedex(None)
	#print("TAB IMG :", dico)
	return render(request, 'moviedex.html', dico)

def leftcursor(request) :
	dico = generate_moviedex('left')
	return HttpResponseRedirect('/moviedex/')
	#return render(request, 'moviedex.html', dico)

def rightcursor(request) :
	dico = generate_moviedex('right')
	return HttpResponseRedirect('/moviedex/')
	#return render(request, 'moviedex.html', dico)

## battle
def battle(request):
	game = Game()
	title = game.get_random_movie().title
	file = open('./moviemon/moviemon_fight', 'w')
	file.write(title)
	file.close()
	return (render(request, 'battle_{}.html'.format(title)))

def throw_ball(request):
	game = Game()
	with open('moviemon/current_save.save') as file:
		game.load(file.read())
	file = open('./moviemon/moviemon_fight', 'r')
	title = file.read()
	list_of_moviemons = scr.load_all_moviemons()
	for mvm in list_of_moviemons:
		if mvm.title == title:
			curr_mvm = mvm
			break
	if (catch_movie(game, curr_mvm)):
		game.moviedex.append(mvm.title)
		print('CAPTURED {}'.format(mvm.title))
	if (game.movieballs > 0):
		game.movieballs -= 1
	game.print_game()
	game.write_infos()
	return (HttpResponseRedirect('/worldmap/'))
