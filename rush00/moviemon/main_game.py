import random
from . import generate_map as g_map
from django.conf import settings

def find_movieballs():
	found_movieball = random.randint(0, 9)
	if (found_movieball == 0):
		print('found movieball')
		file_content = g_map.get_file_content()
		nb_of_balls = file_content[1]
		file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
		file_content[1] = file_content[1].replace(nb_of_balls, str(int(nb_of_balls) + 1)) + '\n'
		for elem in file_content:
			file.write(elem)
		file.close()

def main_game():
	find_movieballs()

