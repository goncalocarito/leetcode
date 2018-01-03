# Description: https://leetcode.com/problems/roman-to-integer/description/

# Code

import unittest


class Solution:
    def romanToInt(self, s):  # time complexity 0(n)
        """
        :type s: str
        :rtype: int
        """
        out = 0
        decipher = {"I": 1, "V": 5, "X": 10, "L": 50,
                    "C": 100, "D": 500, "M": 1000}
        i = 0
        numlen = len(s)
        while i != numlen:
            if i != numlen - 1 and decipher[s[i+1]] > decipher[s[i]]:
                out -= decipher[s[i]]
                i = i+1
            out += decipher[s[i]]
            i = i+1
        return out


# Tests

class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().romanToInt("DCXXI")
        self.assertEqual(res, 621)

    def test_2(self):
        print("test2")
        res = Solution().romanToInt("IV")
        self.assertEqual(res, 4)

    def test_3(self):
        print("test3")
        res = Solution().romanToInt("MCMXCVI")
        self.assertEqual(res, 1996)


if __name__ == '__main__':
    unittest.main()
