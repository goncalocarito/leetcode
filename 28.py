# Description: https://leetcode.com/problems/remove-element/description/

# Code

import unittest


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
# Tests


class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().strStr("hello", "ll")
        self.assertEqual(res, 2)

    def test_2(self):
        print("test2")
        res = Solution().strStr("aaaaaa", "abc")
        self.assertEqual(res, -1)


if __name__ == '__main__':
    unittest.main()
