#The problem includes very large inputs, so i used short test cases for demonstration.
import unittest
from trapping_rain_water import Solution

class TestTrappingRainWater(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.trap([0,1,0,2]), 1)
        self.assertEqual(self.solution.trap([3,0,2,0,4]), 7)
        self.assertEqual(self.solution.trap([1,0,1]), 1)
        
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.trap([]), 0)
        self.assertEqual(self.solution.trap([5]), 0)
        self.assertEqual(self.solution.trap([2,2,2,2]), 0)
        self.assertEqual(self.solution.trap([0,1,2,3]), 0)
        self.assertEqual(self.solution.trap([4,3,2,1]), 0)

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)