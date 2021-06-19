def write_columns(up_map, columns, pos_y):
	for i in range(columns):
		up_map.write('\t<td back>\n')
		if (pos_y == i):
			up_map.write("""\t\t<img src="{% static 'sacha.jpg' %}" height=30 width=30 style="text-align: center; vertical-align: middle;">\n""")
		else:
			up_map.write("""\t\t<img src="{% static 'grass.jpg' %}" height=30 width=30>\n""")
		up_map.write('\t</td>\n')

def generate_map(player_pos, rows, columns):
	up_map = open('./templates/map.html', 'w')

	up_map.write('{% extends "base.html" %}\n')
	up_map.write('{% block title %}\n')
	up_map.write('Map\n')
	up_map.write('{% endblock %}\n')
	up_map.write('{% load static %}\n')
	up_map.write('{% block style %}\n')
	up_map.write("""<link rel="stylesheet" type="text/css" href="{% static 'map_style.css' %}">\n""")
	up_map.write('{% endblock %}')
	up_map.write('{% block content %}\n')
	up_map.write("""<table>\n""")

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
	generate_map([5, 5], 20, 20)