import random
from django.conf import settings
from .imdb_scraper import *

class Game:
    #current pos = [int, int]
    #number of movieballs  = int
    #names of the moviemons = list
    #informations = dict
    def __init__(self) :
        self.pos = [0, 0]
        self.movieballs = 0
        self.moviedex = []
        self.moviemons_infos = []
        self.strenght = 0 #A modi!!!

    def load(self, content) :
        # print("content : ", content)
        lines = content.split('\n')
        info_pos = lines[0].split(',') #Parse first lines player pos format "x,y"
        self.pos[0] = int(info_pos[0])
        self.pos[1] = int(info_pos[1])
        del lines[0]
        self.movieballs = int(lines[0]) #Parse first lines player pos format "amout"
        del lines[0]
        if lines[0] != "_void_" : #if no moviedex the informations is set to "_void_"
            list_moviedex = lines[0].split(",")
            for moviemon in list_moviedex :  #
                self.moviedex.append(moviemon)
        del lines[0]
       # print("movieballs : ", lines[0])
        for l in lines :
            self.moviemons_infos.append(self.getMoviemons(l))
        
        #teestt
        #print(self.pos)
        #print(self.movieballs)
        #print(self.moviedex)
        #print(self.moviemons_infos)
        return self
            
    def get_random_movie(self):
        # l = []
        # for movi in self.moviemons_infos :
        #     if movi['title'] not in self.moviedex :
        #         l.append(movi)
        # if len(l) == 0 :
        #     return None
        # nb = random(0, len(l) - 1)
        # return l[nb]
        list_of_mons = load_all_moviemons()
        i = random.randint(0, 9)
        return (list_of_mons[i])

    def load_default_settings(self) :
        self.pos[0] = settings.STARTING_POINT[0]
        self.pos[1] = settings.STARTING_POINT[1]
        self.movieballs = 0
        self.moviedex = []
        list_of_moviemons = load_all_moviemons()
        self.moviemons_infos = list_of_moviemons

        return self

    def get_strength(self) :
        return self.strenght

    def get_movie(self, title) :
        moviemon = {}
       # print("title :", title)
        for mov in self.moviemons_infos :
            #print("title mov:", mov.title)
            if title == mov.title :
                moviemon['title'] = mov.title
                moviemon['director'] = mov.director
                moviemon['year'] = mov.year
                moviemon['rating'] = mov.rating
                moviemon['synopsis'] = mov.synopsis
                moviemon['poster'] = mov.poster
        return moviemon

    def getMoviemons(self, line) :
        d = {}
        split = line.split('|')
        for elem in split :
            #print(elem)
            pair = elem.split('*')
            d[pair[0]] = pair[1]
        mov = Moviemon(d)
        return mov

    def write_infos(self) :
        new_content = ""
        new_content += "{0},{1}\n".format(str(self.pos[0]), str(self.pos[1]))
        new_content += "{0}\n".format(str(self.movieballs))
        if (len(self.moviedex) == 0) :
            new_content += "_void_\n"
        else :
            i = 0
            for mov in self.moviedex :
                new_content += "{0}".format(str(mov))
                if i < len(self.moviedex) - 1 :
                    new_content += ','
                i += 1
            new_content += "\n"
        i = 0
        for moviemon in self.moviemons_infos :
            new_content += "title*{0}|director*{1}|year*{2}|rating*{3}|actors*{4}|synopsis*{5}|poster*{6}".format(\
            moviemon.title, moviemon.director, moviemon.year, moviemon.rating, moviemon.actors, moviemon.synopsis, moviemon.poster)
            if i < len(self.moviemons_infos) - 1:
                new_content += '\n'
            i+=1
        with open ('moviemon/current_save.save', 'w+') as file :
            file.write(new_content)

    def print_game(self) :
        print("Pos :", str(self.pos))
        print("balls :", str(self.movieballs))
        print("films deja pris :", str(self.moviedex))
        for m in self.moviemons_infos :
            print(m)
    