
from sqlalchemy import create_engine

from source_code import sql_conn
from sql_commands import tables

class PostgresHandler:

	# class variables ...
	postgres_url = sql_conn # <-- PostgresSQL connection password and username parameters from {source_code.py}

	def __init__(self):

		# instance variables ...git
		self.engine = create_engine(self.postgres_url)
		self.table = tables['metadata_table']
		self.create_table() # <-- Definitely, this function is always running when the PostgresHandler will be called!

	def create_table(self):

		# --------------- Add values [New Style formatting] -----------------
		# create_statement = "...{table_name}..."
		# self.table = tables['metadata_table'] # <-- from instance variables
		# create_statement.format(table_name = self.table)
		# -------------------------------------------------------------------

		create_statement = """
		select count (*) from information_schema. tables t 
		where t.table_name = '{table_name}'
		"""
		try:
			with self.engine.connect() as conn:
				for self.table, cre_script in tables.items():

					temp = conn.execute(create_statement.format(table_name = self.table))

					if temp.fetchone()[0] == 0:
						conn.execute(cre_script)

						# In Console the Python returns information about creation of DataBase in PostgresSQL ...
						print("The {table_name} has been created!".format(table_name = str(tables.keys())))
		except:

			print("The {table_name} already Exist!".format(table_name = tables.keys()))

if __name__ == '__main__':
	test = PostgresHandler()
