import unittest
from smallest_number_set_bits import Solution

class TestSmallestNumberSetBits(unittest.TestCase):
    
    def setUp(self):
        """Create solution before test"""
        self.solution = Solution()
        
    def test_basic(self):
        """Test basic cases"""
        self.assertEqual(self.solution.smallestNumber(5), 7)
        self.assertEqual(self.solution.smallestNumber(10), 15)
        self.assertEqual(self.solution.smallestNumber(3), 3)
        
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.smallestNumber(1), 1)
        self.assertEqual(self.solution.smallestNumber(7), 7)
        self.assertEqual(self.solution.smallestNumber(8), 15)
    
    def test_larger_numbers(self):
        """Test larger numbers"""
        self.assertEqual(self.solution.smallestNumber(16), 31)
        self.assertEqual(self.solution.smallestNumber(100), 127)
    
if (__name__ == '__main__'):
    unittest.main()