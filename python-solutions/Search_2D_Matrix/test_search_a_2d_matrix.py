import unittest
from search_a_2d_matrix import Solution

class TestSearchA2DMatrix(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.searchMatrix([[1,3,5],[7,9,11],[13,15,17]], 9), True)
        self.assertEqual(self.solution.searchMatrix([[1,3,5],[7,9,11],[13,15,17]], 2), False)
    
    def test_edge(self):
        """Test edge cases"""
        self.assertEqual(self.solution.searchMatrix([], 1), False)
        self.assertEqual(self.solution.searchMatrix([[5]], 5), True)
        self.assertEqual(self.solution.searchMatrix([[5]], 2), False)
        self.assertEqual(self.solution.searchMatrix([[1,2,3],[4,5,6]], 1), True)
        self.assertEqual(self.solution.searchMatrix([[1,2,3],[4,5,6]], 6), True)
        self.assertEqual(self.solution.searchMatrix([[1,2,3],[4,5,6]], 7), False)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)
    