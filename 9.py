# Description: https://leetcode.com/problems/palindrome-number/description/

# Code

import unittest


class Solution:
    # space complexity 0(n)
    # time complexity 0(n)
    # faster
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]

    # space complexity 0(1)
    # time complexity 0(n)
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + int(x % 10)
            x = int(x / 10)

        return x == revertedNumber or x == int(revertedNumber / 10)


# Tests

class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().isPalindrome(121)
        self.assertEqual(res, True)

    def test_2(self):
        print("test2")
        res = Solution().isPalindrome(1423)
        self.assertEqual(res, False)

    def test_3(self):
        print("test3")
        res = Solution().isPalindrome(987656789)
        self.assertEqual(res, True)

    def test_4(self):
        print("test4")
        res = Solution().isPalindrome(1534236469)
        self.assertEqual(res, False)

    def test_5(self):
        print("test5")
        res = Solution().isPalindrome(123321)
        self.assertEqual(res, True)

    def test_6(self):
        print("test6")
        res = Solution().isPalindrome(1001)
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
