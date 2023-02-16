"""
FILE DESCRIPTION:
This file content, the PostgresSQL commands in order to easier handling within the package.

----------------------------------------------------------------------------------------------- [INCOMING DATA FORMULA]
from {.json} get data from website :

data = {
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
-------------------------------------------------------------------------------------------------- [list data formula]


------------------------------------------------------------------------------------------------------------------------
"""
#-------------------------------------------------------------------------------------------------- [CREATE STATEMENTS]
create_movies_table = """CREATE TABLE IF NOT EXISTS movies(
	adult boolean,
	backdrop_path text,
	id integer primary key,
	original_language varchar(10),
	original_title varchar(100),
	overview text,
	popularity real,
	poster_path varchar(100),
	release_date date,
	title varchar(100),
	video boolean,
	vote_average real,
	vote_count integer
	)
	"""
# Nested list handling ...
create_genre_id_table = """CREATE TABLE IF NOT EXISTS  genre_ids(
	id integer,
	genre_id integer,
	CONSTRAINT movies
	FOREIGN KEY (id)
	REFERENCES movies(id)
	)
"""
# Data enrichment ...
create_data_location_table = """CREATE TABLE IF NOT EXISTS  data_location(
	id integer,
	poster_location text,
	movie_location text,
	CONSTRAINT movies
	FOREIGN KEY (id)
	REFERENCES movies (id)
	)
"""
# -------------------------------------------------------------------------------------------------- [Table dictionary]
tables = {
	'metadata_table': create_movies_table,
	'genre_id_table': create_genre_id_table,
	'data_location': create_data_location_table
}

# ------------------------------------------------------------------------------------------------- [INSERT STATEMENTS]

insert_movie_table = """
INSERT INTO movies(
adult,
backdrop_path,
id,
original_language,
original_title,
overview,
popularity,
poster_path,
release_date,
title,
video,
vote_average,
vote_count
) 
VALUES(
:adult, 
:backdrop_path,
:id,
:original_language,
:original_title,
:overview,
:popularity,
:poster_path,
:release_date,
:title,
:video,
:vote_average,
:vote_count
)

"""
insert_genre_id_table = """
INSERT INTO genre_ids(
id, 
genre_id
)
VALUES(
:id,
:genre_id
)
"""
# Data enrichment ...
insert_location_table = """
INSERT INTO data_location(
id,
poster_location,
movie_location
)
VALUES(
%s,
%s,
%s
)
"""
select_original_title_in_db = """
SELECT original_title FROM movies;
"""