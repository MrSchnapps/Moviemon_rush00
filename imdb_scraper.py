import requests, json, sys

class Moviemon():
	def __init__(self, scraped_info):
		self.title = scraped_info['title']
		self.director = scraped_info['director']
		self.year = scraped_info['year']
		self.rating = scraped_info['rating']
		self.actors = scraped_info['actors']
		self.synopsis = scraped_info['synopsis']

def scrape_imdb(movie_name):
	url = 'http://www.omdbapi.com/?t={}&apikey=f72e10ff'.format(movie_name)

	S = requests.session()
	page = S.get(url)
	data = page.json()

	scrape_dic = {}
	scrape_dic['title'] = data['Title']
	scrape_dic['director'] = data['Director']
	scrape_dic['year'] = data['Year']
	scrape_dic['rating'] = data['imdbRating']
	scrape_dic['actors'] = data['Actors']
	scrape_dic['synopsis'] = data['Plot']

	return(scrape_dic)

Moviemon1-title:title-director:director-
Moviemon2-