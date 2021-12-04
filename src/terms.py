class OrderAnnotation(object):

	def __init__(self, order):
		self.order = order

	def __str__(self):
		return str(self.order)

	def __repr__(self):
		return repr(self.order)

	def __getitem__(self, i):
		return self.order[i]


class Term(object):

	def __init__(self, oa, lst):
		# an order annotation serves as the functor of the term
		self.oa = oa
		# list of the children
		self.lst = lst

	def __str__(self):
		# TODO: visualization of the terms
		return str(self.oa)

	def __len__(self):
		return len(self.lst)


