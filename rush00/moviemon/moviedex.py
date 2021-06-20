#from .writers import *
from .Game import *

def generate_moviedex(move) :
	game = Game()
   
	with open ("moviemon/save1_example", 'r') as file :
		game.load(file.read())
	#file = open("moviemon/files_utils/moviedex.infos", 'w')
	#file.close()
	with open("moviemon/files_utils/moviedex.infos", 'r') as file:
		lines = file.readlines()
	if len(lines) == 0 :
		cursor = 0
	else :
		cursor = int(lines[0])

	#-------------
	#with open('moviemon/templates/moviedex.html', 'w') as file :
	tab_img = []
	tab_cursor = []
	for mon in game.moviedex :
		#print(game.get_movie(mon)['poster'])
		#for mv in game.moviemons_infos :
			#print(mv.poster)
		tab_img.append((game.get_movie(mon))['poster'])
	if move == 'right' :
		if cursor < len(tab_img) - 1 :
			cursor += 1
	elif move == 'left' :
		if cursor > 0 :
			cursor -= 1
	#elif move == None :
	#	print ("WSH")
		#cursor = 0
	for mon in tab_img :
		tab_cursor.append('0')
	tab_cursor[cursor] = '1'
	dico = {'cursor':tab_cursor, 'imgs':tab_img}
	with open("moviemon/files_utils/moviedex.infos", 'w') as file:
		file.write(str(cursor))
	return dico
