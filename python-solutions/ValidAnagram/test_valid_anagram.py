import unittest
from valid_anagram import Solution

class TestValidAnagram(unittest.TestCase):
    
    def setUp(self):
        """Create solution"""
        self.solution = Solution()
    
    def test_valid_anagrams(self):
        """Test valid anagrams"""
        self.assertEqual(self.solution.isAnagram("fried", "fired"), True)
        self.assertEqual(self.solution.isAnagram("car", "arc"), True)
        self.assertEqual(self.solution.isAnagram("listen", "silent"), True)

    def test_invalid_anagrams(self):
        """Test invalid anagrams"""
        self.assertEqual(self.solution.isAnagram("sad", "happy"), False)
        self.assertEqual(self.solution.isAnagram("best", "worst"), False)
        self.assertEqual(self.solution.isAnagram("python", "javascript"), False)
    
    def test_edge_cases(self):
        """Test edge cases"""
        self.assertEqual(self.solution.isAnagram("a", "ab"), False)
        self.assertEqual(self.solution.isAnagram("", ""), True)
        self.assertEqual(self.solution.isAnagram("aaa", "aaa"), True)
        self.assertEqual(self.solution.isAnagram("aab", "abb"), False)
        self.assertEqual(self.solution.isAnagram("A","a"), False)
        
        

if (__name__ == '__main__'):
    unittest.main(verbosity = 2)