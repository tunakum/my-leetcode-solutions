import unittest
from three_sum import Solution

class TestThreeSum(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""        
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.threeSum([-1,0,1,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(self.solution.threeSum([0,1,1]), [])
        self.assertEqual(self.solution.threeSum([0,0,0]), [[0,0,0]])
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.threeSum([ ]), [])
        self.assertEqual(self.solution.threeSum([0]), [])
        self.assertEqual(self.solution.threeSum([1, -1]), [])
        self.assertEqual(self.solution.threeSum([1,1,1,1]), [])

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)