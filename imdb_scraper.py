import requests, json, sys

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
