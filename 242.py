# Description: https://leetcode.com/problems/valid-anagram/description/

# Code

import unittest


class Solution:
    def isAnagram1(self, s, t):  # O(nlogn)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):  # O(n)
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counS, counT = {}, {}
        for i in s:
            if i in counS:
                counS[i] += 1
            else:
                counS[i] = 1
        for i in t:
            if i in counT:
                counT[i] += 1
            else:
                counT[i] = 1
        return counS == counT


# Tests

class TestSolution(unittest.TestCase):
    def test_1(self):
        res = Solution().isAnagram1("anagram", "nagaram")
        self.assertEqual(res, True)

    def test_2(self):
        res = Solution().isAnagram1("rat", "car")
        self.assertEqual(res, False)

    def test_3(self):
        res = Solution().isAnagram1("", "")
        self.assertEqual(res, True)

    def test_4(self):
        res = Solution().isAnagram2("anagram", "nagaram")
        self.assertEqual(res, True)

    def test_5(self):
        res = Solution().isAnagram2("rat", "car")
        self.assertEqual(res, False)

    def test_6(self):
        res = Solution().isAnagram2("", "")
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
