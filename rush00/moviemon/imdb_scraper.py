import requests, json, sys

class Moviemon():
	def __init__(self, scraped_info):
		self.title = scraped_info['title']
		self.director = scraped_info['director']
		self.year = scraped_info['year']
		self.rating = scraped_info['rating']
		self.actors = scraped_info['actors']
		self.synopsis = scraped_info['synopsis']
		self.poster = scraped_info['poster']

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
	scrape_dic['poster'] = data['Poster']

	return(scrape_dic)

if __name__ == '__main__':
	scrape_imdb(sys.argv[1])