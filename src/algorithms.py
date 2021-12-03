from terms import Term
from termdep import Tree

def is_projective_naive(tree):
	""" 
	The following algorithm tests whether the input tree is
	projective in a naive way, i.e., it runs in quadratic time 
	rather than linear.

	The naive algorithm works as follows.
	For every head--dependency pair (h1, d1),
	we check whether there exists another head--dependency 
	pair (h2, d2) that could interleave in a non-projective way. 
	Since we conider all pairs, we only need to consider four cases: 
	i)   h1, h2, d1, d2
	ii)  h1, d2, d1, h2
	iii) d2, h1, h2, d1
	iv)  h2, h1, d2, d1
	"""
	for n1 in range(len(tree)):
		(h1, d1) = tree[n1]
		for n2 in range(len(tree)):
			(h2, d2) = tree[n2]
			# cases (i) and (ii)
			if h1 < h2 and ((h2 < d1 < d2) or (d2 < d1 < h2)):
				return False
			# cases (iii) and (iv)
			if d2 < d1 and ((d2 < h1 < h2) or (h2 < h1 < d2)):
				return False
	return True

# projectivity test (linear algorithm)
def is_projective(tree):
	pass

# pre-order collect (page 32)
def pre_order_collect(tree):
	pass

# post-order collect (page 32)
def post_order_collect(tree):
	pass

# treelet-order collect (page 34)
def treelet_order_collect(tree):
	pass

# Extract-Order-Annotations (page 29)
def extract_order_annotations(tree):
	"""
	The following algorithm extracts the order annotations 
	of the given tree in linear time. 
	Given a tree, it returns a list of order annotations as lists 
	according to its precedence.
	e.g. for the tree ((-1, 2), (1, 0), (2, 1), (2, 3)) 
	it returns [[0], [0,1], [1,2,3], [3]]
	"""
	prec = [None] * len(tree) 
	order = [None] * len(tree)

	#Fill out precedence array
	for u in range(len(tree)):
		(h, d) = tree[u]
		prec[d] = u
		order[u] = []
	#Calculate the order
	for x in range(len(prec)):
		(h, d) = tree[prec[x]]
		if h != -1 :
			order[h].append(d)  
		order[x].append(d)
	return order

# tree to term (Chapter 3)
def encode_proj(tree):

	rootnode = -1
	order_annotations = extract_order_annotations(tree)

	for u in range(len(tree)):
		(h, d) = tree[u]
		if h == -1 :
			rootnode = u

	def term(root): 
		oa = [j+1 for j in range(len(order_annotations[root])-1)]
		lst = []

		for i, node in enumerate(order_annotations[root]):
			if node == root:
				oa = oa.insert(i,0)
			else:
				lst.append(term(node))
		
		return Term(tuple(oa), tuple(lst))

	return term(rootnode)

# term to tree (Chapter 3)
def decode_proj(term):

	pass