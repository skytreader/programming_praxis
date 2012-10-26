#! usr/bin/env python

import sys

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
		self.table = []
		first = True
		
		with open(filename, "r") as table_file:
			for table_row in table_file:
				if not first:
					self.table.append(table_row.split("	"))
				
				first = False
	
	def get_key(self, rowno):
		"""
		Returns the contents of the key field of the specified
		row.
		"""
		return self.table[rowno][0]

def row_by_key(table, key):
	"""
	Returns a list of all the rows in the given table associated
	with the given key.
	"""
	fitting_rows = []
	
	for row in table:
		if row[0] == key:
			fitting_rows.append(row)
	
	return fitting_rows

def natural_join(table1, table2):
	"""
	Given two tables, join them on their keys.
	"""
	joined = []
	
	for row in table1:
		matching_rows = row_by_key(table2, row[0])
		
		for match in matching_rows:
			row.extend(match[1:len(match)])
			joined.append(row)
	
	return joined

if __name__ == "__main__":
	table1 = Table(sys.argv[1])
	table2 = Table(sys.argv[2])
	print(natural_join(table1.table, table2.table))
