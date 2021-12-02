
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
    pass

# tree to term (Chapter 3)


def encode_proj(tree):
    pass

# term to tree (Chapter 3)


def decode_proj(term):
    pass
