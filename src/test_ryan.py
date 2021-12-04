from algorithms import *

# projective trees
proj = []
proj.append(((-1, 0), (0, 4), (1, 3), (3, 2), (4, 1)))
proj.append(((0, 1), (1, 2), (-1, 0)))
proj.append(((0, 1), (1, 2), (-1, 3), (3, 0)))
proj.append(((-1, 0), (5, 4), (1, 5), (0, 1), (2, 3), (4, 2)))
proj.append(((2, 1), (3, 2), (-1, 3), (3, 9), (3, 5),
         (5, 4), (5, 6), (6, 8), (8, 7), (1, 0)))
proj.append(((1, 2), (2, 3), (4, 1), (5, 4), (5, 7), (8, 5), (7, 6),
         (1, 0), (-1, 8), (8, 13), (13, 9), (10, 11), (13, 12), (13, 10)))
proj.append(((2, 1), (-1, 2), (2, 5), (2, 3), (1, 0), (5, 4)))
proj.append(((1, 0), (-1, 1), (1, 3), (3, 2), (1, 4), (4, 6), (6, 5)))


t = encode_proj(proj[1])
d = decode_proj(t)

def compare(lst1, lst2):
	set1, set2 = set(lst1), set(lst2)
	for s in set1:
		assert s in set2
	for s in set2:
		assert s in set1

for p in proj:
	t = encode_proj(p)
	d = decode_proj(t)
	compare(p, d)

