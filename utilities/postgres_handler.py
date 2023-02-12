
from sqlalchemy import create_engine
from sqlalchemy import text

from .source_code import sql_conn
from .sql_commands import (
							tables,
							insert_movie_table,
							insert_genre_id_table,
							insert_location_table,
							select_original_title_in_db
							)
from .file_handler import Filehandler

class PostgresHandler:

	def __init__(self):
		self.engine = create_engine(sql_conn)
		self.create_table()
		self.table = tables
		self.file_handler = Filehandler()

	def create_table(self):
		"""
		This func. creates {table_name} table in PostgreSQL database by dinamicaly from tables {} contents.
		"""

		# --------------- Add values [New Style formatting] -----------------
		# create_statement = "...{table_name}..."
		# self.table = tables['metadata_table'] # <-- from instance variables
		# create_statement.format(table_name = self.table)
		# -------------------------------------------------------------------

		select_statement = """select count(*) from information_schema. tables t
		where t.table_name = '{table_name}'"""

		# print(select_statement.format(table_name = self.table)) # <-- only debuging!

		with self.engine.connect() as conn:
			for table, cre_script in tables.items():
				temp = conn.execute(select_statement.format(table_name = table))

				if temp.fetchone()[0] == 0:
					conn.execute(cre_script)

	def insert_data(self, data):
		# print(data)
		# print("---------------------------------------------")
		poster_loc_data = self.file_handler.get_poster_location()
		# # poster_loc_data = [
		# # 		# 'D:\\PROJECTS\\metadata_store_in_postgres\\posters\\Alien.jpg',
		# # 		# 'D:\\PROJECTS\\metadata_store_in_postgres\\posters\\American Pie.jpg',
		# # 		# 'D:\\PROJECTS\\metadata_store_in_postgres\\posters\\Bad Boys.jpg',
		# # 		# 'D:\\PROJECTS\\metadata_store_in_postgres\\posters\\Ghost.jpg',
		# # 		# 'D:\\PROJECTS\\metadata_store_in_postgres\\posters\\Lion king.jpg'
		# # 		# ]
		# print(poster_loc_data)
		movie_loc_data = self.file_handler.get_movie_location()


		# print(data)
		with self.engine.connect() as conn:
			try:
				# insert data in {movies_table} ...
				conn.execute(text(insert_movie_table), data)

				# create genre_ids data ...
				genre_ids = [{'id': data['id'], 'genre_id': item} for item in data['genre_ids']]

				# insert genre data in {genre_ids} table ...
				conn.execute(text(insert_genre_id_table), genre_ids)

				# create Poster, and movie path data insertion list as location ...
				location = [int(data['id']), data['poster_location'], data['movie_location']]

				# insert location data in {data_location} table ...
				conn.execute(insert_location_table, location)

			except Exception as e:
				print(str(e))

	def delete_data(self):
		with self.engine.connect() as conn:
			conn.execute('delete from genre_ids')
			conn.execute('delete from movies')
			conn.execute('delete from data_location')

if __name__ == '__main__':

	test = PostgresHandler()
	test.create_table()

	test_data = {
    "adult": 'False',
    "backdrop_path": "/3RJ0B8JnwuOaQf6qmwTILXibcJj.jpg",
    "genre_ids": [
        28,
        878,
        14
    ],
    "id": '941520',
    "original_language": "en",
    "original_title": "Alien Sniperess",
    "overview": "A female sniper on military leave promises ...",
    "popularity": '193.478',
    "poster_path": "/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg",
    "release_date": "2022-04-08",
    "title": "Alien Sniperess",
    "video": 'False',
    "vote_average": '3.9',
    "vote_count": '13'
	}
	# test.delete_data()
	# test.insert_data(test_data)
	test.select_data()
