import random
from . import generate_map as g_map
from django.conf import settings
from . import Game

def find_movieballs(game):
	found_movieball = random.randint(0, 9)
	if (found_movieball == 0):
		game.movieballs += 1
		game.write_infos()
		return (1)
	return (0)

def find_moviemon():
	found_moviemon = random.randint(0, 4)
	if (found_moviemon == 0):
		return (1)
	return (0)

def main_game(game):
	if not find_movieballs(game):
		return (find_moviemon())


