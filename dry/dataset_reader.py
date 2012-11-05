#! usr/bin/env python

# TODO Test!

class DatasetReader(object):
	"""
	Parse all sorts of data sets. For special use in Programming
	Praxis data sets.
	"""
	
	def __init__(self, filename):
		self.__file = open(filename)
	
	@property
	def column_delimeter(self):
		"""
		The regular expression which delimits columns.
		"""
		return self.__column_delimiter
	
	def get_data(self):
		"""
		Return an iterable which is the parsed form of the
		next line in the data set.
		"""
		pass
	
	def close(self):
		self.__file.close()

class OffsetReader(DatasetReader):
	"""
	For data sets where the first n lines are actually pretty-printing
	stuff (column headers, bars, etc.)
	"""
	# TODO Can I reference parent's fields with self? :\	
	def __init__(self, line_offset, col_delimiter, filename):
		super(OffsetReader, self).__init__(filename)
		super(OffsetReader, self).__column_delimiter = col_delimiter
		
		for i in range(line_offset):
			super(OffsetReader, self).__file.read()
	
	def get_data(self):
		file_line = super(OffsetReader, self).__file.read()
		return file_line.split(super(OffsetReader, self).__column_delimiter)
