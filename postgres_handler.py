
from sqlalchemy import create_engine
from source_code import connection_params

class PostgresHandler:

	postgres_url = connection_params

	def __init__(self):

		self.engine = create_engine(self.postgres_url) # <-- PostgresSQL connection password and username parameters

	"""
	Data formula from {.json} data
		{
	    "adult": false,
	    "backdrop_path": "/3RJ0B8JnwuOaQf6qmwTILXibcJj.jpg",
	    "genre_ids": [                                        <--- NESTED LIST
	        28,
	        878,
	        14
	    ],
	    "id": 941520,
	    "original_language": "en",
	    "original_title": "Alien Sniperess",
	    "overview": "A female sniper on military leave promises ...",
	    "popularity": 193.478,
	    "poster_path": "/bI1ZDRkerXrcaFa5kWjEMw80aqE.jpg",
	    "release_date": "2022-04-08",
	    "title": "Alien Sniperess",
	    "video": false,
	    "vote_average": 3.9,
	    "vote_count": 13
	}
	"""
	def create_table(self):
		pass


if __name__ == '__main__':
	pass