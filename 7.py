# Description: https://leetcode.com/problems/reverse-integer/description/

# Code

import unittest


class Solution:
    def reverse(self, x):  # 0(n)
        """
        :type x: int
        :rtype: int
        """
        sig = 1 if x > 0 else -1
        y = x*sig
        res = str(abs(x))[::-1]
        if y == x:
            res = int(res)
        else:
            res = -int(res)
        if res < -2147483647 or res > 2147483648:
            return 0
        return res


# Tests

class TestSolution(unittest.TestCase):
    def test_1(self):
        res = Solution().reverse(123)
        self.assertEqual(res, 321)

    def test_2(self):
        res = Solution().reverse(-123)
        self.assertEqual(res, -321)

    def test_3(self):
        res = Solution().reverse(120)
        self.assertEqual(res, 21)

    def test_4(self):
        res = Solution().reverse(1534236469)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
