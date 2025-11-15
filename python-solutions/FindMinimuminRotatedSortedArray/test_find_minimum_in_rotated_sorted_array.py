import unittest
from find_minimum_in_rotated_sorted_array import Solution

class TestFindMinimumInRotatedSortedArray(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
        
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.findMin([3,4,5,1,2]), 1)
        self.assertEqual(self.solution.findMin([4,5,6,7,0,1,2]), 0)
        self.assertEqual(self.solution.findMin([11,13,15,17]), 11)
        self.assertEqual(self.solution.findMin([2,3,4,5,1]), 1)
        
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.findMin([10]), 10)
        self.assertEqual(self.solution.findMin([2,1]), 1)
        self.assertEqual(self.solution.findMin([1,2]), 1)
        self.assertEqual(self.solution.findMin([30,40,50,10,20]), 10)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)