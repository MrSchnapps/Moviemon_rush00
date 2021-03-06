from django.conf import settings
from . import main_game
import sys
from . import Game

def write_columns(up_map, columns, pos_y):
	i = 0
	while (i < columns):
		up_map.write('\t<td>\n')
		if (pos_y == i):
			up_map.write("""\t\t<img src="{% static 'sacha.jpg' %}" height=30 width=30 style="text-align: center; vertical-align: middle;">\n""")
		else:
			up_map.write("""\t\t<img src="{% static 'grass.jpg' %}" height=30 width=30>\n""")
		up_map.write('\t</td>\n')
		i += 1

def generate_map(pos_x, pos_y, rows, columns, found_moviemon, game):
	pos_x = int(pos_x)
	pos_y = int(pos_y)
	rows = int(rows)
	columns = int(columns)
	if (pos_x < 0):
		pos_x = 0
	if (pos_x > rows - 1):
		pos_x = rows - 1
	if (pos_y < 0):
		pos_y = 0
	if (pos_y > columns - 1):
		pos_y = columns - 1
	up_map = open(str(settings.BASE_DIR.joinpath('moviemon/templates/map.html')), 'w')

	up_map.write('{% extends "base.html" %}\n')
	up_map.write('{% block title %}\n')
	up_map.write('Map\n')
	up_map.write('{% endblock %}\n')
	up_map.write('{% load static %}\n')
	up_map.write('{% block style %}\n')
	up_map.write("""<link rel="stylesheet" type="text/css" href="{% static 'map_style.css' %}">\n""")
	up_map.write('{% endblock %}\n')
	up_map.write('{% block screen %}\n')
	up_map.write("""<table>\n""")
	up_map.write("<p>{} movieballs<p>\n".format(game.movieballs))
	up_map.write("<p>Moviemons caught : {}</p>\n".format(game.moviedex))

	i = 0
	while (i < rows):
		up_map.write('<tr>\n')
		if (pos_x == i):
			write_columns(up_map, columns, pos_y)
		else:
			write_columns(up_map, columns, -1)
		up_map.write('</tr>\n')
		i += 1

	up_map.write('</table>\n')
	up_map.write('{% endblock %}\n')
	up_map.write("""{% block control %}\n\
<ul>\n\
	<li><button onclick="location.href = '/moveup'">Up</button></li>\n\
    <li><button onclick="location.href = '/movedown'">Down</button></li>\n\
    <li><button onclick="location.href = '/moveleft'">Left</button></li>\n\
    <li><button onclick="location.href = '/moveright'">Right</button></li>\n\
    <li><button onclick="location.href = '/moviedex'">Select</button></li>\n\
	<li><button onclick="location.href = '/worldmap'">Start</button></li>\n\
	<li><button onclick="location.href = '/worldmap'">A</button></li>\n\
	<li><button onclick="location.href = '/worldmap'">B</button></li>\n\
    \n\
</ul>\n\
{% endblock %}\n""")

def get_file_content():
	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'r')
	file_content = file.readlines()
	file.close()
	return (file_content)

def get_pos(file_content):
	pos = file_content[0].split(',')
	return (pos)

def move_character(direction):
	game = Game.Game()
	with open('moviemon/current_save.save') as file:
		game.load(file.read())
	if (direction == 'up'):
		if (game.pos[0] > 0):
			game.pos[0] -= 1
	elif (direction == 'down'):
		if (game.pos[1] < settings.ROWS - 1):
			game.pos[0] += 1
	elif (direction == 'left'):
		if (game.pos[1] > 0):
			game.pos[1] -= 1
	elif (direction == 'right'):
		if (game.pos[1] < settings.COLUMNS - 1):
			game.pos[1] += 1
	generate_map(game.pos[0], game.pos[1], settings.ROWS, settings.COLUMNS, 0, game)
	game.write_infos()
	return (main_game.main_game(game))

# def move_character_up(pos_x, pos_y):
# 	file_content = get_file_content()
# 	pos = get_pos(file_content)
# 	curr_x = int(pos[0])
# 	new_x = int(pos[0]) - 1
# 	found_moviemon = 0
# 	if (new_x >= 0):
# 		file_content[0] = file_content[0].replace(str(curr_x)+',', str(new_x)+',')
# 		found_moviemon = (main_game.main_game())
# 	generate_map(int(pos[0]) - 1, int(pos[1]), settings.ROWS, settings.COLUMNS, found_moviemon)
# 	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
# 	for elem in file_content:
# 		file.write('{}'.format(elem))
# 	file.close()

# def move_character_down():
# 	file_content = get_file_content()
# 	pos = get_pos(file_content)
# 	found_moviemon = 0
# 	curr_x = int(pos[0])
# 	new_x = int(pos[0]) + 1
# 	if (new_x < settings.ROWS):
# 		file_content[0] = file_content[0].replace(str(curr_x)+',', str(new_x)+',')
# 		found_moviemon = main_game.main_game()
# 	generate_map(int(pos[0]) + 1, int(pos[1]), settings.ROWS, settings.COLUMNS, found_moviemon)
# 	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
# 	for elem in file_content:
# 		file.write('{}'.format(elem))
# 	file.close()
	

# def move_character_left():
# 	file_content = get_file_content()
# 	pos = get_pos(file_content)
# 	found_moviemon = 0
# 	curr_x = int(pos[1])
# 	new_x = int(pos[1]) - 1
# 	if (new_x >= 0):
# 		file_content[0] = file_content[0].replace(','+str(curr_x), ','+str(new_x))
# 		found_moviemon = main_game.main_game()
# 	generate_map(int(pos[0]), int(pos[1]) - 1, settings.ROWS, settings.COLUMNS, found_moviemon)
# 	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
# 	for elem in file_content:
# 		file.write('{}'.format(elem))
# 	file.close()
	

# def move_character_right():
# 	file_content = get_file_content()
# 	pos = get_pos(file_content)
# 	found_moviemon = 0
# 	curr_x = int(pos[1])
# 	new_x = int(pos[1]) + 1
# 	if (new_x < settings.COLUMNS): # number of columns
# 		file_content[0] = file_content[0].replace(','+str(curr_x), ','+str(new_x))
# 		found_moviemon = main_game.main_game()
# 	generate_map(int(pos[0]), int(pos[1]) + 1, settings.ROWS, settings.COLUMNS, found_moviemon)
# 	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
# 	for elem in file_content:
# 		file.write('{}'.format(elem))
# 	file.close()
	

if __name__ == '__main__':
	generate_map(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], 0)