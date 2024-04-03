import unittest
import sys
sys.path.append('.')
from SimpleProblem3.Cody import UniqueList

import unittest
import sys
sys.path.append('.')
from SimpleProblem3.Cody import UniqueList

class TestUniqueList(unittest.TestCase):

    def test_empty_list(self):
        my_list = []
        unique_list = UniqueList(my_list).get_unique_list()
        self.assertEqual(len(unique_list), 0)

    def test_single_value_list(self):
        my_list = [1] 
        unique_list = UniqueList(my_list).get_unique_list()
        self.assertEqual(unique_list, [1])

    def test_duplicates(self):
        my_list = [1, 2, 2, 3]
        unique_list = UniqueList(my_list).get_unique_list()
        self.assertEqual(unique_list, [1, 2, 3])
        
    def test_unhashable_types(self):
        my_list = [{'a': 1}, {'a': 1}]
        unique_list = UniqueList(my_list).get_unique_list()
        self.assertEqual(unique_list, [{'a': 1}, {'a': 1}])

if __name__ == '__main__':
    unittest.main()
