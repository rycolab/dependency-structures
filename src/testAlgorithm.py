import unittest
from algorithms import *


# projective trees
proj1 = ((-1, 0), (0, 4), (1, 3), (3, 2), (4, 1))
proj2 = ((0, 1), (1, 2), (-1, 0))
proj3 = ((0, 1), (1, 2), (-1, 3), (3, 0))
proj4 = ((-1, 0), (5, 4), (1, 5), (0, 1), (2, 3), (4, 2))
proj5 = ((2, 1), (3, 2), (-1, 3), (3, 9), (3, 5),
         (5, 4), (5, 6), (6, 8), (8, 7), (1, 0))
proj6 = ((1, 2), (2, 3), (4, 1), (5, 4), (5, 7), (8, 5), (7, 6),
         (1, 0), (-1, 8), (8, 13), (13, 9), (10, 11), (13, 12), (13, 10))
proj7 = ((2, 1), (-1, 2), (2, 5), (2, 3), (1, 0), (5, 4))
proj8 = ((1, 0), (-1, 1), (1, 3), (3, 2), (1, 4), (4, 6), (6, 5))

# non-projective trees
nonproj1 = ((1, 3), (2, 0), (0, 1), (-1, 2))
nonproj2 = ((1, 0), (-1, 1), (0, 2))
nonproj3 = ((-1, 0), (2, 3), (3, 1), (0, 2))
nonproj4 = ((2, 0), (-1, 1), (1, 2), (0, 3))
nonproj5 = ((0, 2), (1, 0), (-1, 1))
nonproj6 = ((0, 2), (3, 4), (-1, 0), (4, 1), (2, 3))

# pre/post order collect example from book
poc1 = ((0, 1), (-1, 0), (1, 2), (2, 3), (0, 4))

# tree well-formedness tests
missingroot1 = ((0, 1), (1, 2), (2, 3), (0, 4))
doublydependent1 = ((2, 1), (-1, 2), (2, 5), (2, 3), (1, 0), (5, 4), (4, 3))
notconnected1 = ((2, 3), (-1, 0), (3, 2), (0, 1))
notconnected2 = ((2, 4), (-1, 0), (3, 2), (0, 1), (4, 3))
tworoots1 = ((1, 2), (2, 3), (4, 1), (5, 4), (5, 7), (8, 5), (7, 6), (-1, 6),
             (1, 0), (-1, 8), (8, 13), (13, 9), (10, 11), (13, 12), (13, 10))
doubleedge1 = ((-1, 0), (5, 4), (1, 5), (0, 1), (2, 3), (1, 5), (4, 2))
missingdependency1 = ((2, 1), (3, 2), (-1, 3), (3, 9),
                      (3, 5), (5, 4), (5, 6), (6, 8), (8, 7))
missingdependency2 = ((1, 0), (-1, 1), (1, 3), (3, 2), (1, 4), (4, 7), (7, 5))

# order annotations
ord1 = [[0, 4], [1, 3], [2], [2, 3], [1, 4]]
ord2 = [[0,1], [1, 2], [2]]
ord3 = [[0, 1], [1,2], [2], [0, 3]]
ord4 = [[0,1], [1,5], [2,3], [3], [2,4], [4,5]]
ord5 = [[0], [0,1], [1,2], [2,3,5,9], [4], [4,5,6], [6,8], [7], [7,8], [9]]
ord6 = [[0], [0,1,2], [2,3], [3], [1,4], [4,5,7], [6], [6,7],
         [5,8,13], [9], [10, 11], [11], [12], [9,10,12,13]]
ord7 = [[0], [0, 1], [1,2,3,5], [3], [4], [4, 5]]
ord8 = [[0], [0,1,3,4], [2], [2,3], [4, 6], [5], [5, 6]]

term1 = Term((0, 1), Term((1, 0), Term((0, 1), Term((1,0), Term((0), ())))))

def tree_dict(tree):
    td = {}
    for (parent, child) in tree:
        td[child] = parent
    return td


class TestProjectivity(unittest.TestCase):

    def test_projective_naive(self):
        self.assertEqual(is_projective_naive(proj1), True)
        self.assertEqual(is_projective_naive(proj2), True)
        self.assertEqual(is_projective_naive(proj3), True)
        self.assertEqual(is_projective_naive(proj4), True)
        self.assertEqual(is_projective_naive(proj5), True)
        self.assertEqual(is_projective_naive(proj6), True)
        self.assertEqual(is_projective_naive(proj7), True)
        self.assertEqual(is_projective_naive(proj8), True)

    def test_non_projective_naive(self):
        self.assertEqual(is_projective_naive(nonproj1), False)
        self.assertEqual(is_projective_naive(nonproj2), False)
        self.assertEqual(is_projective_naive(nonproj3), False)
        self.assertEqual(is_projective_naive(nonproj4), False)
        self.assertEqual(is_projective_naive(nonproj5), False)
        self.assertEqual(is_projective_naive(nonproj6), False)

    def test_projective_linear(self):
        self.assertEqual(is_projective(proj1), True)
        self.assertEqual(is_projective(proj2), True)
        self.assertEqual(is_projective(proj3), True)
        self.assertEqual(is_projective(proj4), True)

    def test_non_projective_linear(self):
        self.assertEqual(is_projective(nonproj1), False)
        self.assertEqual(is_projective(nonproj2), False)
        self.assertEqual(is_projective(nonproj3), False)
        self.assertEqual(is_projective(nonproj4), False)
        self.assertEqual(is_projective(nonproj5), False)
        self.assertEqual(is_projective(nonproj6), False)

    def test_pre_order_collect(self):
        self.assertEqual(pre_order_collect(poc1), [0, 1, 2, 3, 4])

    def test_post_order_collect(self):
        self.assertEqual(post_order_collect(poc1), [3, 2, 1, 4, 0])

    def test_is_well_formed(self):
        self.assertEqual(is_well_formed(proj1), True)
        self.assertEqual(is_well_formed(proj2), True)
        self.assertEqual(is_well_formed(proj3), True)
        self.assertEqual(is_well_formed(proj4), True)
        self.assertEqual(is_well_formed(proj5), True)
        self.assertEqual(is_well_formed(proj6), True)
        self.assertEqual(is_well_formed(proj7), True)
        self.assertEqual(is_well_formed(proj8), True)
        self.assertEqual(is_well_formed(nonproj1), True)
        self.assertEqual(is_well_formed(nonproj2), True)
        self.assertEqual(is_well_formed(nonproj3), True)
        self.assertEqual(is_well_formed(nonproj4), True)
        self.assertEqual(is_well_formed(nonproj5), True)
        self.assertEqual(is_well_formed(nonproj6), True)
        self.assertEqual(is_well_formed(poc1), True)
        self.assertEqual(is_well_formed(missingroot1), False)
        self.assertEqual(is_well_formed(doublydependent1), False)
        self.assertEqual(is_well_formed(notconnected1), False)
        self.assertEqual(is_well_formed(notconnected2), False)
        self.assertEqual(is_well_formed(tworoots1), False)
        self.assertEqual(is_well_formed(doubleedge1), False)
        self.assertEqual(is_well_formed(missingdependency1), False)
        self.assertEqual(is_well_formed(missingdependency2), False)



class TestAlgorithms(unittest.TestCase):

    def test_extract_order_annotations(self):
        self.assertEqual(extract_order_annotations(proj1), ord1)
        self.assertEqual(extract_order_annotations(proj2), ord2)
        self.assertEqual(extract_order_annotations(proj3), ord3)
        self.assertEqual(extract_order_annotations(proj4), ord4)
        self.assertEqual(extract_order_annotations(proj5), ord5)
        self.assertEqual(extract_order_annotations(proj6), ord6)
        self.assertEqual(extract_order_annotations(proj7), ord7)
        self.assertEqual(extract_order_annotations(proj8), ord8)
    
    def test_extract_order_annotations(self):
        def compare_terms(term0, term1):
            
            self.assertTupleEqual(term0.oa, term1.oa)
            #self.assertEqual(len(term0.lst), len(term1.lst))
            for i in range(len(term0.lst)):
                compare_terms(term0.lst[i], term1.lst[i])

            compare_terms(encode_proj(proj1), term1)
    def test_get_lca(self):
        self.assertEqual(get_lca(tree_dict(proj1), 4, 3), 4)   
        self.assertEqual(get_lca(tree_dict(proj1), 4, 0), 0) 
        self.assertEqual(get_lca(tree_dict(proj1), 2, 4), 4) 
        self.assertEqual(get_lca(tree_dict(proj1), 3, 2), 3)
        self.assertEqual(get_lca(tree_dict(proj1), 3, 4), 4)   
        self.assertEqual(get_lca(tree_dict(proj1), 0, 4), 0) 
        self.assertEqual(get_lca(tree_dict(proj1), 4, 2), 4) 
        self.assertEqual(get_lca(tree_dict(proj1), 2, 3), 3) 

if __name__ == '__main__':
    unittest.main()

