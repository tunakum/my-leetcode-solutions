import unittest
from product_of_array_except_self import Solution

class TestProductOfArrayExceptSelf(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_basic(self):
        """Test normal-basic cases"""
        self.assertEqual(self.solution.productExceptSelf([1,2,3,4]), [24,12,8,6])
        self.assertEqual(self.solution.productExceptSelf([2,3,4,5]), [60,40,30,24])

    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.productExceptSelf([1,2,0,4]), [0,0,8,0])
        self.assertEqual(self.solution.productExceptSelf([0,4,0]), [0,0,0])
        self.assertEqual(self.solution.productExceptSelf([-1,1,-1,1]), [-1,1,-1,1])

    def test_additional(self):
        """Additional tests (not edge but different inputs)"""
        self.assertEqual(self.solution.productExceptSelf([2,2,2,2]), [8,8,8,8])
        self.assertEqual(self.solution.productExceptSelf([3,1,5]), [5,15,3])

if(__name__ == "__main__"):
    unittest.main(verbosity = 2)