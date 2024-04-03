import unittest

class TestCody(unittest.TestCase):

    def test_empty_list(self):
        lst = []
        self.assertEqual(find_largest_integer(lst), None)

    def test_list_with_one_element(self):
        lst = [5] 
        self.assertEqual(find_largest_integer(lst), 5)

    def test_list_with_duplicates(self):
        lst = [1, 5, 2, 5, 3]
        self.assertEqual(find_largest_integer(lst), 5)

    def test_list_with_strings(self):
        lst = [1, 'a', 3]
        with self.assertRaises(TypeError):
            find_largest_integer(lst)

    def test_nested_list(self):
        lst = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(find_largest_integer(lst), 6)

import unittest

class TestSelectedCode(unittest.TestCase):

    def test_empty_list(self):
        lst = []
        self.assertEqual(find_largest(lst), None)

    def test_single_element_list(self):
        lst = [5] 
        self.assertEqual(find_largest(lst), 5)

    def test_list_with_duplicates(self):
        lst = [1, 5, 2, 5, 3]
        self.assertEqual(find_largest(lst), 5)

    def test_list_with_strings(self):
        lst = ['a', 'b', 'c']
        self.assertRaises(TypeError, find_largest, lst)

    def test_list_with_floats(self):
        lst = [1.1, 5.5, 2.2]
        self.assertEqual(find_largest(lst), 5.5)
class TestUniqueList(unittest.TestCase):

    def test_empty_list(self):
        my_list = []
        unique_list = []
        
        Cody.unique(my_list, unique_list)
        
        self.assertEqual(len(unique_list), 0)

    def test_single_value_list(self):
        my_list = [1]
        unique_list = []
        
        Cody.unique(my_list, unique_list)
        
        self.assertEqual(unique_list, [1])

    def test_all_unique_values(self):
        my_list = [1, 2, 3]
        unique_list = []
        
        Cody.unique(my_list, unique_list)
        
        self.assertEqual(unique_list, [1, 2, 3])

    def test_duplicates(self):
        my_list = [1, 2, 2, 3]
        unique_list = []
        
        Cody.unique(my_list, unique_list)
        
        self.assertEqual(unique_list, [1, 2, 3])

    def test_mixed_types(self):
        my_list = [1, '2', 3.0]
        unique_list = []
        
        Cody.unique(my_list, unique_list)
        
        self.assertEqual(unique_list, [1, '2', 3.0])
