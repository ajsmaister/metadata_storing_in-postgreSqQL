
# Built-in func...
import os
import json

# ------------------------------------------------------------------------------------------ [FILE DESCRIPTION SECTION]
"""
Class Description:

	This class handles the file, and folder operations of App. It creates the necessary folders like:
	[metadata] and [poster]
	First it create {.json} files in {metadata} folder.
	Finally it also writes the {.jpg} files into the poster folder.

"""
class Filehandler:

	# ---------------------------------------------------------------------------------------------- [CLASS ATTRIBUTES]
	# Create posters root lib ...
	poster_folder = os.path.dirname(os.path.dirname(__file__))     # <-- path of movie_metadata_downloader_in_files
	poster_folder_path = os.path.join(poster_folder, 'posters')    # <-- add folder name

	# Create metadata root lib ...
	metadata_folder = os.path.dirname(os.path.dirname(__file__))     # <-- path of movie_metadata_downloader_in_files
	metadata_folder_path = os.path.join(metadata_folder, 'metadata') # <-- add folder name

	# Create movie root lib ...
	movies_folder = os.path.dirname(os.path.dirname(__file__))  # <-- path of movie_metadata_downloader_in_files
	movies_folder_path = os.path.join(movies_folder, 'movies')  # <-- add folder name

	# print(poster_folder_path)   # Only Debugging! <-- class 'str'
	# print(metadata_folder_path) # Only Debugging! <-- class 'str'
	# print(movies_folder_path)   # Only Debugging! <-- class 'str'

	#  -------------------------------------------------------------------------------------------------- [CONSTRUCTOR]
	def __init__(self):

		# instance variables ...
		self.__create_necessary_folder()
		self.json_path = None # <-- Create poster_path variable
		self.poster_path = None

	# ----------------------------------------------------------------------------------------------------- [FUNCTIONS]
	def __create_necessary_folder(self):
		"""
		This function creates necessary folders if they have  NOT already existed in order to save metadata and posters.

		:params1: poster_folder_path,
		:params2: metadata_folder_path,
		:return: poster_folder, metadata_folder

		"""
		if not os.path.exists(self.poster_folder_path):
			os.mkdir(self.poster_folder_path)
		if not os.path.exists(self.metadata_folder_path):
			os.mkdir(self.metadata_folder_path)

	def get_data_from_movies_folder(self):
		"""
		This func. gran files from the movie folder, and makes a list comprehension in order to get the name of movies.
		:param: {movie_folder_path} from the class attributes
		:return: A list with movie names
		"""
		if not os.path.exists(self.movies_folder_path):
			print(f'The {self.movies_folder_path} is NOT exists!')

			# #-----------------/SIMPLE LOOP /--------------------
			# temp = []
			# for item in os.listdir(self.movies_folder_path):
			# 	if item[-4:] == ".mkv":
			# 		temp.append(item[:-4])
			# #---------------------------------------------------

		# Loop with list comprehension:
		movies = [item[:-4] for item in os.listdir(self.movies_folder_path) if item[-4:] == ".mkv"]
		movies_with_extension = [item for item in os.listdir(self.movies_folder_path)]
		return movies, movies_with_extension

	# ------------------------------------------------------------------------------------------------------------------
	def set_json_path(self, movie_name):
		"""
		This func. set the path for {.json} files
		:param movie_name: Incoming params from {movies[] lists}
		                   from  get_data_from_movies_folder() func. in {metadata_postgres_downloader.py}
		:return:           {movie_name.json} path
		"""
		self.json_path = os.path.join(self.metadata_folder_path, f"{movie_name}.json")

	def write_json(self, data):
		"""
		This func. returns the {movie_name.json} file with metadata into the metadata folder
		:param:  data
		:return: {movie_name.json} file
		"""
		try:
			if os.path.exists(self.json_path):
				print(f"The file {self.json_path} is ALREADY Exists!")
				pass

			with open(self.json_path, "w",  encoding = "utf-8") as f:
				json.dump(data, f, ensure_ascii = False, indent = 4)

		except Exception as e:
			str(e)

	# ------------------------------------------------------------------------------------------------------------------

	def set_poster_path(self, movie_name):
		"""
		This func. returns the poster path of the downloaded poster of the movie from movies folder.

		:param movie_name, self.poster_folder_path
		:return: {movie_name}.jpg
		"""
		self.poster_path = os.path.join(self.poster_folder_path, f"{movie_name}.jpg")

	def write_image(self, image_binary):
		# Before use this func. --> call the set_poster_path() func. !!!
		try:
			with open(self.poster_path, "wb",) as poster:
				poster.write(image_binary)
		except Exception as e:
			return False, str(e)
		pass

	def get_poster_location(self):
		"""
		:return: The poster path list from posters folder
		"""

		# ------------------------[ NORMAL LOOPS]-----------------------
		# posters_name = os.listdir(self.poster_folder_path)

		# for item in posters_name:
		# 	poster_path_list.append(f'{self.poster_folder_path}\\{item}')
		# ---------------------------------------------------------------
		# Same as upper, but with list comprehension ...
		# poster_path_list = [f'{self.poster_folder_path}\\{item}' for item in os.listdir(self.poster_folder_path)]

		return [f'{self.poster_folder_path}\\{item}' for item in os.listdir(self.poster_folder_path)]


	def get_movie_location(self):
		"""
		:return: The movie path list from movies folder
		"""

		# ------------------------[ NORMAL LOOP]-----------------------
		# movie_name   = os.listdir(self.movies_folder_path)

		# for item in movie_name:
		# 	movie_path_list.append(f'{self.movies_folder_path}\\{item}')
		# ---------------------------------------------------------------
		# Same as upper, but with list comprehension ...
		# movie_path_list = [f'{self.movies_folder_path}\\{item}' for item in os.listdir(self.movies_folder_path)]

		return [f'{self.movies_folder_path}\\{item}' for item in os.listdir(self.movies_folder_path)]

# =============================================================================== [FILE TEST SECTION {file_handler.py}]

if __name__ == '__main__':

	test = Filehandler()
	# get movie folder content in a list!
	movie_list = test.get_data_from_movies_folder()
	print(movie_list)

	# test write_jason func. ...
	test.set_json_path(movie_name = 'Alien')   # <-- test_movie_name
	test.write_json(data = {"movie": "alien"}) # <-- test_data
	print(test.get_poster_location())
	print(test.get_movie_location())
