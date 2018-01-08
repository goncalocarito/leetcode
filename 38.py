# Description: https://leetcode.com/problems/count-and-say/description/

# Code

import unittest

# list append and then join seems to be a bit faster then string concatenation


class Solution:
    def count(self, num):
        counter = 1
        out = []
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                counter += 1
            else:
                out.append(str(counter))
                out.append(num[i-1])
                counter = 1

        out.append(str(counter))
        out.append(num[-1])

        return ''.join(out)

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        out = "1"
        for i in range(n-1):
            out = Solution().count(out)
        return out

# Tests


class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().countAndSay(1)
        self.assertEqual(res, "1")

    def test_2(self):
        print("test2")
        res = Solution().countAndSay(2)
        self.assertEqual(res, "11")

    def test_3(self):
        print("test3")
        res = Solution().countAndSay(3)
        self.assertEqual(res, "21")

    def test_4(self):
        print("test4")
        res = Solution().countAndSay(4)
        self.assertEqual(res, "1211")



if __name__ == '__main__':
    unittest.main()
