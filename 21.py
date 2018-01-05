# Description:https://leetcode.com/problems/merge-two-sorted-lists/description/

# Code

import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        l3 = pre
        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            l3 = l3.next

        l3.next = l1 or l2
        return pre.next


# Tests

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(1)
l3.next = ListNode(1)
l3.next.next = ListNode(2)
l3.next.next.next = ListNode(3)
l3.next.next.next.next = ListNode(4)
l3.next.next.next.next.next = ListNode(4)


class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().mergeTwoLists(l1, l2)
        self.assertEqual(res.val, l3.val)
        self.assertEqual(res.next.val, l3.next.val)
        self.assertEqual(res.next.val, l3.next.val)
        self.assertEqual(res.next.next.val, l3.next.next.val)
        self.assertEqual(res.next.next.next.val, l3.next.next.next.val)
        self.assertEqual(res.next.next.next.next.val,
                         l3.next.next.next.next.val)
        self.assertEqual(res.next.next.next.next.next.val,
                         l3.next.next.next.next.next.val)


if __name__ == '__main__':
    unittest.main()
