# Description: https://leetcode.com/problems/third-maximum-number/description/

# Code

import unittest


class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = set(nums)
        firstmax = max(snums)
        second = snums - set([firstmax])
        if not second:
            return firstmax
        secondmax = max(second)
        third = snums - set([firstmax]) - set([secondmax])
        if third:
            return max(third)
        else:
            return firstmax


# Tests

class TestSolution(unittest.TestCase):
    def test_1(self):
        res = Solution().thirdMax([3, 2, 1])
        self.assertEqual(res, 1)

    def test_2(self):
        res = Solution().thirdMax([1, 2])
        self.assertEqual(res, 2)

    def test_3(self):
        res = Solution().thirdMax([2, 2, 3, 1])
        self.assertEqual(res, 1)


if __name__ == '__main__':
    unittest.main()
