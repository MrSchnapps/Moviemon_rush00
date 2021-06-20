from .Game import Game
from django.conf import settings
from . import imdb_scraper as scr
import random

def generate_battle(game, moviemon):
	battle = open(str(settings.BASE_DIR.joinpath('moviemon/templates/battle_{}.html'.format(moviemon.title))), 'w')

	battle.write('{% extends "base.html" %}\n')
	battle.write('{% block title %}\n')
	battle.write('Map\n')
	battle.write('{% endblock %}\n')
	battle.write('{% load static %}\n')
	battle.write('{% block style %}\n')
	battle.write("""<link rel="stylesheet" type="text/css" href="{% static 'map_style.css' %}">\n""")
	battle.write('{% endblock %}\n')
	battle.write('{% block screen %}\n')
	battle.write('<p><img src={} /></p>\n'.format(moviemon.poster))
	battle.write('<p>Moviemon strength : {}</p>\n'.format(moviemon.rating))
	battle.write('<p>Movieballs : {}</p>\n'.format(game.movieballs))
	battle.write('<p>Player strength : {}</p>\n'.format(game.strenght))
	winning_rate = catch_movie(game, moviemon)
	battle.write('<p>Winning rate : {}</p>\n'.format(winning_rate))
	battle.write('{% endblock %}\n')
	battle.write("""{% block control %}\n\
<ul>\n\
	<li><button>Up</button></li>\n\
    <li><button>Down</button></li>\n\
    <li><button>Left</button></li>\n\
    <li><button>Right</button></li>\n\
    <li><button onclick="location.href = '/moviedex'">Select</button></li>\n\
	<li><button>Start</button></li>\n\
	<li><button onclick="location.href = '/throw_ball'">A</button></li>\n\
	<li><button onclick="location.href = '/worldmap'">B</button></li>\n\
    \n\
</ul>\n\
{% endblock %}\n""")

def catch_movie(game, moviemon):
	game = Game()
	with open('moviemon/current_save.save') as file:
		game.load(file.read())
	if (game.movieballs <= 0):
		return
	C = 50 - (float(moviemon.rating) * 10) + (int(game.strenght) * 5)
	if (C > 90):
		C = 90
	if (C < 1):
		C = 1
	rnd = random.randint(1, 100)
	if (C >= rnd):
		return (1)
	return (0)