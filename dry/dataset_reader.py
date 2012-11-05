#! usr/bin/env python

class DatasetReader(object):
	"""
	Parse all sorts of data sets. For special use in Programming
	Praxis data sets.
	"""
	
	@property
	def line_offset(self):
		return self.__line_offset
	
	@property
	def column_delimeter(self):
		return self.__column_delimiter
	
	def get_data(self):
		"""
		Return an iterable which is the parsed form of the
		next line in the data set. Return null if we have already
		iterated through all the lines in the data set.
		"""
		pass
