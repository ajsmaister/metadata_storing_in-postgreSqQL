
"""
File Description:
This file content the web connection, and web operation func. It downloads the metadata of movies, from{url}
"""
import tmdbsimple as tmdb
from urllib.request import urlopen
from movie_metadata_downloader_in_files.source_code import key, image_server_url

class SearchModule:

	# class atributes:
	tmdb.API_KEY = key              # <-- from source_code.py [it is NOT in git!]
	image_server = image_server_url # <-- from source_code.py [it is NOT in git!]

	def __init__(self, search_obj: tmdb.Search):

		# Creates class object from parameter ...
		self.search      = search_obj
		self.poster_path = None

	def search_movie(self, title):
		movie_meta = self.search.movie(query = title)['results']
		if not movie_meta:
			return False
		self.poster_path = movie_meta[0]['poster_path']
		return movie_meta[0]

	def get_image_obj_in_binary(self):
		"""
		This func. download the binary code of images
		:return: img. binary object.
		"""
		return urlopen( f"{self.image_server}{self.poster_path}").read()

# ============================================================================== [FILE TEST SECTION {search_module.py}]

if __name__ == '__main__':
	searc_obj = tmdb.Search()
	test = SearchModule(searc_obj)
	print(test.search_movie('Alien'))
	print(test.get_image_obj_in_binary())

