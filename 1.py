# Description: https://leetcode.com/problems/two-sum/description/

# Code

import unittest


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hidx = {}
        for i, n in enumerate(nums):
            if target - n in hidx:
                return [hidx[target - n], i]
            else:
                hidx[n] = i
        return [-1, -1]


# Tests

class TestSolution(unittest.TestCase):
    def test_thirdMax1(self):
        res = Solution().twoSum([2, 7, 11, 15], 9)
        self.assertEqual(res, [0, 1])

    def test_thirdMax2(self):
        res = Solution().twoSum([3, 2, 4], 6)
        self.assertEqual(res, [1, 2])

    def test_thirdMax3(self):
        res = Solution().twoSum([3, 3], 6)
        self.assertEqual(res, [0, 1])


if __name__ == '__main__':
    unittest.main()
