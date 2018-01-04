# Description: https://leetcode.com/problems/valid-parentheses/description/

# Code

import unittest


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        invtable = {")": "(",
                    "}": "{",
                    "]": "["}
        stack = []
        for c in s:
            if c in invtable.values():
                stack.append(c)
            elif not stack or invtable[c] != stack[-1]:
                return False
            else:
                stack.pop()
        return not stack


# Tests

class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().isValid("()")
        self.assertEqual(res, True)

    def test_2(self):
        print("test2")
        res = Solution().isValid("(){}[]")
        self.assertEqual(res, True)

    def test_3(self):
        print("test3")
        res = Solution().isValid("(]")
        self.assertEqual(res, False)

    def test_4(self):
        print("test4")
        res = Solution().isValid("([)]")
        self.assertEqual(res, False)

    def test_5(self):
        print("test5")
        res = Solution().isValid("([{}])")
        self.assertEqual(res, True)

    def test_6(self):
        print("test6")
        res = Solution().isValid("(")
        self.assertEqual(res, False)

    def test_7(self):
        print("test7")
        res = Solution().isValid("[])")
        self.assertEqual(res, False)

    def test_8(self):
        print("test8")
        res = Solution().isValid("([]{})")
        self.assertEqual(res, True)

    def test_9(self):
        print("test9")
        res = Solution().isValid("(()(")
        self.assertEqual(res, False)

    def test_10(self):
        print("test10")
        res = Solution().isValid("{{)}")
        self.assertEqual(res, False)

    def test_11(self):
        print("test11")
        res = Solution().isValid("[({(())}[()])]")
        self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
