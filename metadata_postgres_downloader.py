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
from utilities.postgres_handler import PostgresHandler


def metadata_loader():
	"""
	:return: metadata and .jpg image in porsters folders, finally it return the downloaded items
	"""
	# Create search object ..
	search_obj   = tmdb.Search()
	file_handler = Filehandler()
	search       = SearchModule(search_obj)
	postgres     = PostgresHandler()

	# Get  movies[0] list length ...
	movies       = file_handler.get_data_from_movies_folder()
	cnt_movies   = len(file_handler.get_data_from_movies_folder()[0])

	# Get length  of poster folder content list...
	cnt_poster   = len(os.listdir(file_handler.poster_folder_path))
	poster_name  = os.listdir(file_handler.poster_folder_path)

	movies[1].reverse() # <-- add reversed movies name with extensions in a list in order to create movie path.

	# Downolading-driver loop...
	for item in movies[0]:

		# pass that movies which have poster ...
		if f'{item}.jpg' in poster_name:
			pass
		else:
			# Download data from url ...
			data = search.search_movie(item)

			# image_path ...
			file_handler.set_poster_path(item)

			# Image Download ...
			binary_img = search.get_image_obj_in_binary()

			# Write image ...
			file_handler.write_image(image_binary = binary_img)

			# add poster_location to data ...
			data['poster_location'] = f'{file_handler.poster_path}'

			# Add movie_location to data ...
			data['movie_location']  = f'{file_handler.movies_folder_path}\\{movies[1].pop()}'

			postgres.insert_data(data) # <-- return data in database!

		# Finally the app informs and counts the downloaded movie data ..
	path = file_handler.get_poster_location()
	# print(path) # <-- Debug only!

	# this loop deletes the poster, if the movie is not in movie folder ...
	for idx, item in enumerate(poster_name):
		try:
			if item[:-4] not in movies[0]:
				os.remove(path[idx])
		except Exception as e:
			str(e)

	if cnt_movies - cnt_poster <= 0:
		print( "\n> There is no NEW image download, and metadata in PostgresSQL")
	else:
		print(f"\n> {str(cnt_movies - cnt_poster)} new .jpg have been downloaded and add metadata in ProgresSQL!")

	# print the finish message ...
	print('\n> The {metadata_postgres_downloader.py} and the{file_handler.py} have been finished!')

# =================================================================== [FILE TEST SECTION {metadate_file_downloader.py}]

if __name__ =='__main__':
	metadata_loader()
