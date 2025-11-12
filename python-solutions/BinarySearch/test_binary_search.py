import unittest
from binary_search import Solution

class TestBinarySearch(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.search([-1,0,3,5,9,12], 9), 4)
        self.assertEqual(self.solution.search([-1,0,3,5,9,12], 2), -1)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.search([], 1), -1)
        self.assertEqual(self.solution.search([5], 5), 0)
        self.assertEqual(self.solution.search([5], 1), -1)
        self.assertEqual(self.solution.search([1, 2], 1), 0) 
        self.assertEqual(self.solution.search([1, 2], 3), -1)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)       