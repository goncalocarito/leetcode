# Description: https://leetcode.com/problems/remove-element/description/

# Code

import unittest


class Solution:
    # solution when it's ok to have trash at the end of the array
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i, nums

    # solution where the array only has the x != val
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return i, nums

# Tests


class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().removeElement([3, 2, 2, 3], 3)
        self.assertEqual(res, 2, [2, 2])

    def test_2(self):
        print("test2")
        res = Solution().removeElement([3, 2, 2, 3, 1], 3)
        self.assertEqual(res, 3, [2, 2, 1])

    def test_3(self):
        print("test3")
        res = Solution().removeElement([3, 3], 3)
        self.assertEqual(res, 0, [])

    def test_4(self):
        print("test4")
        res = Solution().removeElement([3, 1, 2, 3, 1, 2, 3], 3)
        self.assertEqual(res, 4, [1, 2, 1, 2])

    def test_5(self):
        print("test5")
        res = Solution().removeElement([2, 2, 2, 2], 3)
        self.assertEqual(res, 4, [2, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()
