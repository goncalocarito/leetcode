# Description:
# https://leetcode.com/problems/search-insert-position/description/

# Code

import unittest


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return i+1


# Tests


class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().searchInsert([1, 3, 5, 6], 5)
        self.assertEqual(res, 2)

    def test_2(self):
        print("test2")
        res = Solution().searchInsert([1, 3, 5, 6], 2)
        self.assertEqual(res, 1)

    def test_3(self):
        print("test3")
        res = Solution().searchInsert([1, 3, 5, 6], 7)
        self.assertEqual(res, 4)

    def test_4(self):
        print("test4")
        res = Solution().searchInsert([1, 3, 5, 6], 0)
        self.assertEqual(res, 0)



if __name__ == '__main__':
    unittest.main()
