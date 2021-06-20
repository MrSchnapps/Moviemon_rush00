from django.conf import settings
from . import main_game
import sys

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

def generate_map(pos_x, pos_y, rows, columns):
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
    <li><button onclick="location.href = '/worldmap'">Select</button></li>\n\
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

def move_character_up():
	file_content = get_file_content()
	pos = get_pos(file_content)
	generate_map(int(pos[0]) - 1, int(pos[1]), settings.ROWS, settings.COLUMNS)
	curr_x = int(pos[0])
	new_x = int(pos[0]) - 1
	if (new_x >= 0):
		file_content[0] = file_content[0].replace(str(curr_x)+',', str(new_x)+',')
	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
	for elem in file_content:
		file.write('{}'.format(elem))
	file.close()
	main_game.main_game()

def move_character_down():
	file_content = get_file_content()
	pos = get_pos(file_content)
	generate_map(int(pos[0]) + 1, int(pos[1]), settings.ROWS, settings.COLUMNS)
	curr_x = int(pos[0])
	new_x = int(pos[0]) + 1
	if (new_x < settings.ROWS):
		file_content[0] = file_content[0].replace(str(curr_x)+',', str(new_x)+',')
	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
	for elem in file_content:
		file.write('{}'.format(elem))
	file.close()
	main_game.main_game()

def move_character_left():
	file_content = get_file_content()
	pos = get_pos(file_content)
	generate_map(int(pos[0]), int(pos[1]) - 1, settings.ROWS, settings.COLUMNS)
	curr_x = int(pos[1])
	new_x = int(pos[1]) - 1
	if (new_x >= 0):
		file_content[0] = file_content[0].replace(','+str(curr_x), ','+str(new_x))
	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
	for elem in file_content:
		file.write('{}'.format(elem))
	file.close()
	main_game.main_game()

def move_character_right():
	file_content = get_file_content()
	pos = get_pos(file_content)
	generate_map(int(pos[0]), int(pos[1]) + 1, settings.ROWS, settings.COLUMNS)
	curr_x = int(pos[1])
	new_x = int(pos[1]) + 1
	if (new_x < settings.COLUMNS): # number of columns
		file_content[0] = file_content[0].replace(','+str(curr_x), ','+str(new_x))
	file = open(str(settings.BASE_DIR.joinpath('moviemon/save1_example')), 'w')
	for elem in file_content:
		file.write('{}'.format(elem))
	file.close()
	main_game.main_game()

if __name__ == '__main__':
	generate_map(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])