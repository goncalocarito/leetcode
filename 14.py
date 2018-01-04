# Description: https://leetcode.com/problems/roman-to-integer/description/

# Code

import unittest


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        out = ""
        for x in zip(*strs):
            if len(set(x)) > 1:
                return out
            else:
                out += x[0]
        return out


# Tests

class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().longestCommonPrefix([])
        self.assertEqual(res, "")

    def test_2(self):
        print("test2")
        res = Solution().longestCommonPrefix(["abcd", "abc", "ab", "a"])
        self.assertEqual(res, "a")

    def test_3(self):
        print("test3")
        res = Solution().longestCommonPrefix(["aaaaaaa", "aaaaabbbb"])
        self.assertEqual(res, "aaaaa")

    def test_4(self):
        print("test3")
        res = Solution().longestCommonPrefix(["", ""])
        self.assertEqual(res, "")


if __name__ == '__main__':
    unittest.main()
