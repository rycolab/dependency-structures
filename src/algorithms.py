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
    for h1, d1 in tree:
        for h2, d2 in tree:
            # cases i), ii), iii), iv)
            if h1 < h2 < d1 < d2 or h1 < d2 < d1 < h2 or d2 < h1 < h2 < d1 or h2 < h1 < d2 < d1:
                return False
    return True


# tests if a tree is well formed
def is_well_formed(tree):
    # find the root and create adjacency list
    root = -1
    children = {}
    vertices = []
    for parent, child in tree:
        vertices.append(child)
        if parent == -1:
            if root != -1:
                # multiple root pointers bad
                return False
            root = child

        # add to adjacency list
        if parent in children.keys():
            if child not in children[parent]:
                # if this is false it would mean a duplicate edge, which we can handle
                # otherwise append
                children[parent].append(child)
        else:
            children[parent] = [child]
        if child not in children.keys():
            children[child] = []

    if len(tree) != len(set(vertices)):
        # there should be n unique nodes as well as n edges
        return False

    if max(vertices) != len(vertices)-1:
        return False

    # if there is no root pointer, return false
    if root == -1:
        return False

    # perform dfs to check if graph is connected
    visited = [False]*len(vertices)

    def dfs(u):
        visited[u] = True

        for v in children[u]:
            if visited[v]:
                return False
            else:
                if not dfs(v):
                    return False
        return True

    if not dfs(root):
        return False

    for b in visited:
        if not b:
            return False
    return True

# projectivity test (linear algorithm)
def is_projective(tree):

    # according to chapter 3.3.2, we can test whether a dependency structure D is projective
    # by computing D' := dep(term(D)), i.e. using the algorithms from the book to turn D first
    # into a term and them this term back into a dependency structure.
    # D is isomorphic to D' if and only if D is projective

    # O(n), see algorithms & proofs in book
    dep = decode_proj(encode_proj(tree))

    # we test the equality/isomorphism of tree and dep by checking whether for all nodes in
    # tree and dep, their parents match
    dict1 = {}
    dict2 = {}

    # dict1 contains for every node d1 from tree its parent h1
    for (h1, d1) in tree:  # O(n)
        dict1[d1] = h1

    # dict2 contains for every node d2 from dep its parent h2
    for (h1, d1) in dep:  # O(n)
        dict2[d1] = h1

    for i in range(len(tree)):  # O(n)
        if dict1[i] != dict2[i]:  # dict lookup in python is O(1) on average
            return False

    return True

# pre-order collect (page 32)
def pre_order_collect(tree):
    # algorithm according to book
    children = {}
    for (i, j) in tree:
        if i in children.keys():
            children[i].append(j)
        else:
            children[i] = [j]
        if j not in children.keys():
            children[j] = []

    def poc(u):
        l = []
        if u != -1:
            l.append(u)
        for v in children[u]:
            l += poc(v)
        return l
    return poc(-1)


# post-order collect (page 32)
def post_order_collect(tree):
    # algorithm according to book
    children = {}
    for (i, j) in tree:
        if i in children.keys():
            children[i].append(j)
        else:
            children[i] = [j]
        if j not in children.keys():
            children[j] = []

    def poc(u):
        l = []
        for v in children[u]:
            l += poc(v)
        if u != -1:
            l.append(u)
        return l
    return poc(-1)


def treelet_ordered_tree(tree):
    # returns a dictionary that encodes a treelet ordered tree
    # in the dictionary, each node u in the tree is annotated with a list that
    # contains the nodes in the treelet rooted at u in the intended order. the
    # "intended order" in our case is just the numerical ordering of the
    # nodes

    t = {}
    for (i, j) in tree:
        if i in t.keys():
            t[i].append(j)
        else:
            t[i] = [j]

    for i in len(tree):
        if i in t.keys():
            t[i].append(i)
        else:
            t[i] = [i]
        t[i] = sorted(t[i])

    return t


# treelet-order collect (page 34)
def treelet_order_collect(tree):
    # algorithm from book
    order = treelet_ordered_tree(tree)

    def toc(u):
        l = []
        for v in order[u]:
            if v == u:
                l.append(u)
            else:
                l += toc(v)
        return l

    return toc(-1)


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

	# fill out precedence array
	for u in range(len(tree)):
		(h, d) = tree[u]
		prec[d] = u
		order[u] = []

	# calculate the order
	for x in range(len(prec)):
		(h, d) = tree[prec[x]]
		if h != -1 :
			order[h].append(d)  
		order[x].append(d)

	return order

# tree to term (Chapter 3)
def encode_proj_old(tree):
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

	# fill out precedence array
	for u in range(len(tree)):
		(h, d) = tree[u]
		prec[d] = u
		order[u] = []

	# calculate the order
	for x in range(len(prec)):
		(h, d) = tree[prec[x]]
		if h != -1 :
			order[h].append(d)  
		order[x].append(d)
	return order


# tree to term (Chapter 3)
def encode_proj(tree):

	# extract the order annotations
	rootnode = -1
	order_annotations = extract_order_annotations(tree)

	# find the root
	for u in range(len(tree)):
		(h, d) = tree[u]
		if h == -1 :
			rootnode = d

	def term(root): 

		oa = [j+1 for j in range(len(order_annotations[root])-1)]
		lst = []
		for i, node in enumerate(order_annotations[root]):
			if node == root:
				oa.insert(i, 0)
			else:
				lst.append(term(node))

		return Term(tuple(oa), tuple(lst))

	return term(rootnode)


# term to tree (Chapter 3)
def decode_proj(term):

	counter, level = -1, 0

	def descend(term, counter, level, deps):

		parent, children = None, []
		for a, t in zip(term.oa, term.lst):
			if a == 0:
				counter += 1
				parent = counter
				if level == 0:
					deps.append((-1, parent))
			else:
				child, counter = descend(t, counter, level+1, deps)
				children.append(child)

		for child in children:
			deps.append((parent, child))

		return parent, counter	

	deps = []
	descend(term, counter, level, deps)
	return tuple(deps)


# TODO: Kuhlmann and Satta (2009)
def annotate_l(tree):
	pass

# analogus to the above, should be combined into one method
def annotator_r(tree):
	pass

def lcas(tree):
	""" 
	Least common ancestor. Can be done in O(|pi|) time.
	See Kuhlmann and Satta (2009)
	"""
	pass

# TODO: Page 38
def block_order_collect(order):
	pass

def encode_block(tree):
	pass

def decode_block(tree):
	pass

# Chapter 5
def is_weakly_nonprojective(tree):
    for i in range(len(tree)):
        for j in range(i+1, len(tree)):
            if min(tree[i]) != -1:
                # case (a) from the book (pg. 52)
                if min(tree[i]) < min(tree[j]) < max(tree[i]) < max(tree[j]):
                    return False
                # case (b) from the book (pg. 52)
                if min(tree[j]) < min(tree[i]) < max(tree[j]) < max(tree[i]):
                    return False
    return True

# Chapter 5
def is_wellnested(tree):
    root_term = encode_block(tree)
    
    def check_forbidden_string(term):
        # check for forbidden substring in term OA
        for i in range(len(term.oa) - 3):
            if term.oa[i] == term.oa[i+2] and term.oa[i+1] == term.oa[i+3]:
                return True
        # recursively check children for forbidden substring
        for i in range(len(term.lst)):
            if check_forbidden_string(term.lst[i]):
                return True
        return False
    
    return not check_forbidden_string(root_term)

term1 = Term((0, 1), tuple([Term((1, 0), Term((0, 1), Term((1,0), Term((0), ()))))]))
tree1 = ((-1, 0), (0, 4), (1, 3), (3, 2), (4, 1))

output = encode_proj(tree1)

print(len(output.lst))
