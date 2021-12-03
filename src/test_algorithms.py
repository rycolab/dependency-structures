import unittest
from algorithms import *

# Extract-Order-Annotations 
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

ord1 = [[0, 4], [1, 4], [2, 3], [2], [1, 3]]
ord2 = [[1, 2], [2], [0,1]]
ord3 = [[1,2], [2], [0, 3], [0, 1]]
ord4 = [[0,1], [2,4], [4,5], [1,5], [3], [2,3]]
ord5 = [[0], [0,1], [1,2], [2,3,5,9], [4], [4,5,6], [6,8], [7], [7,8]]
ord6 = [[0], [0,1,2], [2,3], [3], [1,4], [4,5,7], [6], [6,7],
         [5,8,13], [9], [10, 11], [11], [12], [9,10,12,13]]
ord7 = [[0], [0, 1], [1,2,3,5], [3], [4], [4, 5]]
ord8 = [[0], [0,1,3,4], [2], [2,3], [4, 6], [5], [5, 6]]

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
        

if __name__ == '__main__':
    unittest.main()