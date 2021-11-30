
def is_projective_naive(tree):
	""" 
	The following algorithm tests whether the input tree is
	projective in a naive way, i.e., it runs in quadratic time 
	rather than linear.

	The naive algorithm works as follows.
	For every head--dependency pair (h1, d1),
	we check whether there exists another head--dependency 
	pair (h2, d2) that interleaves. 
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

# pre-order collect (page 32)

# post-order collect (page 32)

# treelet-order collect (page 34)

# Extract-Order-Annotations (page 29)

# tree to term (Chapter 3)

# term to tree (Chapter 3)