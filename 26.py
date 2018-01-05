# Description:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Code

import unittest


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = None
        i = 0
        for num in nums:
            if num != curr:
                nums[i] = num
                curr = num
                i += 1
        return i


# Tests


class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().removeDuplicates([1, 1, 2])
        self.assertEqual(res, 2)

    def test_2(self):
        print("test2")
        res = Solution().removeDuplicates([1, 1, 2, 2, 3, 3])
        self.assertEqual(res, 3)


if __name__ == '__main__':
    unittest.main()
