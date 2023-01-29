import unittest
from unittest.mock import patch
from io import StringIO
from bin_search import bin_search, lower_bound, upper_bound, count_elements

class TesteBinSearch(unittest.TestCase):
    def setup():
        pass

    def test_bin_search(self):
        """ bin searching"""

        with patch('sys.stdout', new=StringIO()):
            expected = True
            actual = bin_search(array=[1, 2, 4, 6, 7], left_idx=0, right_idx=4, elem=4)
            self.assertEqual(actual, expected)

            expected = False
            actual = bin_search(array=[1, 2, 4, 6, 7], left_idx=0, right_idx=2, elem=4)
            self.assertEqual(actual, expected)

            expected = True
            actual = bin_search(array=[1, 2, 4, 6, 7], left_idx=0, right_idx=5, elem=7)
            self.assertEqual(actual, expected)

            expected = True
            actual = bin_search(array=[1], left_idx=0, right_idx=1, elem=1)
            self.assertEqual(actual, expected)

            expected = False
            actual = bin_search(array=[-1, 0, 2, 3, 4, 5], left_idx=0, right_idx=3, elem=1)
            self.assertEqual(actual, expected)

    def test_lower_bound(self):
        """ lower bound searching"""

        with patch('sys.stdout', new=StringIO()):
            expected = 2
            actual = lower_bound(array=[1, 2, 4, 6, 7], elem=4)
            self.assertEqual(actual, expected)

            expected = 2
            actual = lower_bound(array=[1, 2, 4, 4, 4, 6, 7], elem=4)
            self.assertEqual(actual, expected)

            expected = 7
            actual = lower_bound(array=[1, 2, 4, 4, 4, 6, 7], elem=9)
            self.assertEqual(actual, expected)

            expected = 0
            actual = lower_bound(array=[1, 2, 4, 4, 4, 6, 7], elem=-9)
            self.assertEqual(actual, expected)

    def test_upper_bound(self):
        """ upper bound searching"""

        with patch('sys.stdout', new=StringIO()):
            expected = 3
            actual = upper_bound(array=[1, 2, 4, 6, 7], elem=4)
            self.assertEqual(actual, expected)

            expected = 5
            actual = upper_bound(array=[1, 2, 4, 4, 4, 6, 7], elem=4)
            self.assertEqual(actual, expected)

            expected = 7
            actual = upper_bound(array=[1, 2, 4, 4, 4, 6, 7], elem=9)
            self.assertEqual(actual, expected)

            expected = 0
            actual = upper_bound(array=[1, 2, 4, 4, 4, 6, 7], elem=-9)
            self.assertEqual(actual, expected)


    def test_count_elements(self):
        """ count element in array"""

        with patch('sys.stdout', new=StringIO()):
            expected = 1
            actual = count_elements(array=[1, 2, 4, 6, 7], elem=4)
            self.assertEqual(actual, expected)

            expected = 3
            actual = count_elements(array=[1, 2, 4, 4, 4, 6, 7], elem=4)
            self.assertEqual(actual, expected)

            expected = 0
            actual = count_elements(array=[1, 2, 4, 4, 4, 6, 7], elem=9)
            self.assertEqual(actual, expected)

            expected = 0
            actual = count_elements(array=[1, 2, 4, 4, 4, 6, 7], elem=-9)
            self.assertEqual(actual, expected)
