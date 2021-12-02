import unittest
from algorithms import *


# projective trees
proj1 = ((-1, 0), (0, 4), (1, 3), (3, 2), (4, 1))
proj2 = ((0, 1), (1, 2), (-1, 0))
proj3 = ((0, 1), (1, 2), (-1, 3), (3, 0))
proj4 = ((-1, 0), (5, 4), (1, 5), (0, 1), (2, 3), (4, 2))

# non-projective trees
nonproj1 = ((1, 3), (2, 0), (0, 1), (-1, 2))
nonproj2 = ((1, 0), (-1, 1), (0, 2))
nonproj3 = ((-1, 0), (2, 3), (3, 1), (0, 2))
nonproj4 = ((2, 0), (-1, 1), (1, 2), (0, 3))
nonproj5 = ((0, 2), (1, 0), (-1, 1))
nonproj6 = ((0, 2), (3, 4), (-1, 0), (4, 1), (2, 3))


class TestProjectivity(unittest.TestCase):

    def test_projective_naive(self):
        self.assertEqual(is_projective_naive(proj1), True)
        self.assertEqual(is_projective_naive(proj2), True)
        self.assertEqual(is_projective_naive(proj3), True)
        self.assertEqual(is_projective_naive(proj4), True)

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


if __name__ == '__main__':
    unittest.main()
