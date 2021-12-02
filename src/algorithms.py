
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
            # cases (i) and (ii)
            # if h1 < h2 and ((h2 < d1 < d2) or (d2 < d1 < h2)):
            #     return False
            # # cases (iii) and (iv)
            # if d2 < d1 and ((d2 < h1 < h2) or (h2 < h1 < d2)):
            #     return False
            if h1 < h2 < d1 < d2 or h1 < d2 < d1 < h2 or d2 < h1 < h2 < d1 or h2 < h1 < d2 < d1:
                return False
    return True

# projectivity test (linear algorithm)


def is_projective(tree):

    dep = decode_proj(encode_proj(tree))

    dict1 = {}
    dict2 = {}

    for (h1, d1) in tree:
        dict1[d1] = h1

    for (h1, d1) in dep:
        dict2[d1] = h1

    for i in range(len(tree)):
        if dict1[i] != dict2[i]:
            return False

    return True

# pre-order collect (page 32)


def pre_order_collect(tree):
    pass

# post-order collect (page 32)


def post_order_collect(tree):
    pass


def treelet_ordered_tree(tree):
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
