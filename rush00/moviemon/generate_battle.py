from . import Game
from django.conf import settings

def generate_battle(game):
	battle = open(str(settings.BASE_DIR.joinpath('moviemon/templates/map.html')), 'w')