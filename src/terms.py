class Term(object):

	def __init__(self, oa, lst):
		# an order annotation serves as the functor of the term
		self.oa = oa
		# list of the children
		self.lst = lst