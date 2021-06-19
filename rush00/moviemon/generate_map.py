def write_columns(up_map, columns, pos_y):
	for i in range(columns):
		up_map.write('\t<td>\n')
		if (pos_y == i):
			up_map.write('\t\t<img src="./images/sacha.png" height=10 width=10>')
		up_map.write('\t</td>\n')

def generate_map(player_pos, rows, columns):
	up_map = open('./templates/map.html', 'w')

	up_map.write('{% extends "base.html" %}\n')
	up_map.write('{% block title %}\n')
	up_map.write('Map\n')
	up_map.write('{% endblock %}\n')
	up_map.write('{% load static %}')
	up_map.write('{% block styles %}')
	# up_map.write('') <link> to style.css
	up_map.write('{% endblock %}\n')
	up_map.write('{% block content %}\n')
	up_map.write('<table>\n')

	for i in range(rows):
		up_map.write('<tr>\n')
		if (player_pos[0] == i):
			write_columns(up_map, columns, player_pos[1])
		else:
			write_columns(up_map, columns, -1)
		up_map.write('</tr>\n')

	up_map.write('</table>\n')
	up_map.write('{% endblock %}\n')

if __name__ == '__main__':
	generate_map([0, 1], 5, 5)