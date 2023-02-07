"""
FILE DESCRIPTION
Task: Organized guiding the FileHandler, and SearchModule classes.

functions: metadata_loader;
return: {.json} and{.jpg} files in metadata folder and poster folder.

"""
# In-built modules -----------------------------------------------------------------------------------------------------
import os

# Third party modules --------------------------------------------------------------------------------------------------
import tmdbsimple as tmdb

# modules from file ----------------------------------------------------------------------------------------------------
from utilities.file_handler import Filehandler
from utilities.search_module import SearchModule

def metadata_loader():
	"""
	:return: .json metadata and .jpg image in porsters folders, finally it return the downloaded items
	"""
	# get from poster folder the actual files number...
	poster_list = os.listdir(os.path.join(os.path.dirname(__file__), 'posters')) # <-- add folder name
	cnt_poster = len(poster_list)

	# Create search object ..
	search_obj = tmdb.Search()
	file_handler = Filehandler()
	search = SearchModule(search_obj)

	# Get movie mame list and count len movies list {len_movies}...
	movies = file_handler.get_data_from_movies_folder()
	cnt_movies = len(movies)

	# Guiding loop...
	for item in movies:
		# Download data from url ...
		data = search.search_movie(item)
		# Set file root [path] ...
		file_handler.set_json_path(item) # <--change!!
		# Write {"movie_name".json} file ...
		file_handler.write_json(data)    # <--change!!
		# image_path ...
		file_handler.set_poster_path(item)
		# Image Download ...
		binary_img = search.get_image_obj_in_binary()
		# Write image ...
		file_handler.write_image(image_binary = binary_img)

	# Return and count the downloaded movie data ...
	if cnt_movies - cnt_poster == 0:
		print( "\n>There is no NEW image, and {.json} metadata")
	else:
		print(f"\n> {str(cnt_movies - cnt_poster)} new .jpg and .json file have been downloaded!")

	# print the finish message ...
	print('\n> The {metadata_postgres_downloader.py} has  has been finished!')


# =================================================================== [FILE TEST SECTION {metadate_file_downloader.py}]

if __name__ =='__main__':
	metadata_loader()
