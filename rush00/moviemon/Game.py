from random import *
from django.conf import settings
from .imdb_scraper import *

class Game :
    #current pos = [int, int]
    #number of movieballs  = int
    #names of the moviemons = list
    #informations = dict
    def __init__(self) :
        self.pos = [0, 0]
        self.movieballs = 0
        self.moviedex = []
        self.moviemons_infos = []
        self.strenght = 5 #A modi!!!

    def load(self, content) :
        print("content : ", content)
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
            
    def get_random_movie() :
        l = []
        for movi in self.moviemons_infos :
            if movi['title'] not in self.moviedex :
                l.append(movi)
        if len(l) == 0 :
            return None
        nb = random(0, len(l) - 1)
        return l[nb]

    def load_default_settings() :
        self.pos[0] = settings.STARTING_POINT[0]
        self.pos[1] = settings.STARTING_POINT[1]
        self.movieballs = 0
        self.moviedex = []
        self.moviemons_infos = []

        return self

    def get_strength() :
        return self.strenght

    def get_movie(title) :
        moviemon = {}
        for mov in self.moviemons_infos :
            if title == mov['title'] :
                moviemon['title'] = mov['title']
                moviemon['director'] = mov['director']
                moviemon['year'] = mov['year']
                moviemon['rating'] = mov['rating']
                moviemon['synopsis'] = mov['synopsis']
                moviemon['poster'] = mov['poster']

    def getMoviemons(self, line) :
        d = {}
        split = line.split('|')
        for elem in split :
            #print(elem)
            pair = elem.split(':')
            d[pair[0]] = pair[1]
        mov = Moviemon(d)
        return mov

    