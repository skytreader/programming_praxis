#! usr/bin/env python

"""
http://programmingpraxis.com/2010/06/15/natural-join/
"""

class Table(object):
	"""
	This class represents and parses tables from text files.
	
	We represent a table as a file; each line is a record, and fields are
	separated by tabs. For simplicity, we’ll assume that the first field
	in each record is the key.
	
	Note: For formatting purposes assume that multiple tabs may be used to
	delimit fields.
	"""
	
	def __init__(self, filename):
		
		# A list-of-lists
		self.rows = []
		
		# FIXME Remember that the first line is actually the col names.
		with open(filename, "r") as table_file:
			for table_row in table_file:
				self.rows = table_row.split("	")
	
	def get_key(self, rowno):
		"""
		Returns the contents of the key field of the specified
		row.
		"""
		return self.rows[rowno][0]

def natural_join(table1, table2):
	"""
	Given two tables, join them on their keys.
	"""
	pass
