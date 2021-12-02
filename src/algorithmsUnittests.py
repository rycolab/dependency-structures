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

pre1 = ((0,1),(-1,0),(1,2),(2,3),(0,4))


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

    # def test_projective_linear(self):
    #     self.assertEqual(is_projective(proj1), True)
    #     self.assertEqual(is_projective(proj2), True)
    #     self.assertEqual(is_projective(proj3), True)
    #     self.assertEqual(is_projective(proj4), True)

    # def test_non_projective_linear(self):
    #     self.assertEqual(is_projective(nonproj1), False)
    #     self.assertEqual(is_projective(nonproj2), False)
    #     self.assertEqual(is_projective(nonproj3), False)
    #     self.assertEqual(is_projective(nonproj4), False)
    #     self.assertEqual(is_projective(nonproj5), False)
    #     self.assertEqual(is_projective(nonproj6), False)

    def test_pre_order_collect(self):
        self.assertEqual(pre_order_collect(pre1), [0, 1, 2, 3, 4])

    def test_post_order_collect(self):
        self.assertEqual(post_order_collect(pre1), [3, 2, 1, 4, 0])


if __name__ == '__main__':
    unittest.main()
