import unittest
import SimpleProblem1.Cody as cody

class TestCody(unittest.TestCase):

    def test_empty_list(self):
        result = cody.find_largest([])
        self.assertEqual(result, None)

    def test_single_element_list(self):
        result = cody.find_largest([5]) 
        self.assertEqual(result, 5)

    def test_all_negative_elements(self):
        result = cody.find_largest([-3, -5, -7])
        self.assertEqual(result, -3)

    def test_mixed_positive_and_negative(self):
        result = cody.find_largest([-2, 4, -6, 8])
        self.assertEqual(result, 8)

    def test_duplicate_elements(self):
        result = cody.find_largest([2, 5, 2, 5])
        self.assertEqual(result, 5)
