#testte biraz detay görüp keşfetmek istediğim için araştırırken gördüğüm (verbosity=2) yi bu teste dahil ediyorum
import unittest
from square_root import Solution

class TestSquareRoot(unittest.TestCase):
    
    def setUp(self):
        """Create solution before test"""
        self.solution = Solution()
    
    def test_perfect_squares(self):
        """Test perfect square numbers"""
        self.assertEqual(self.solution.mySqrt(4), 2)
        self.assertEqual(self.solution.mySqrt(9), 3)
        self.assertEqual(self.solution.mySqrt(16), 4)
    
    def test_not_perfect_squares(self):
        """Test non perfect square numbers"""
        self.assertEqual(self.solution.mySqrt(8), 2)
        self.assertEqual(self.solution.mySqrt(10), 3)
        self.assertEqual(self.solution.mySqrt(11),3)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.mySqrt(0), 0)
        self.assertEqual(self.solution.mySqrt(1),1)
        self.assertEqual(self.solution.mySqrt(2),1)

if (__name__ == '__main__'):
    unittest.main(verbosity = 2)
        