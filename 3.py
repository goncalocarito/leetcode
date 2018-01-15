# Description:
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Code

import unittest


class Solution:
    # worst case scenario is 0(n^3)
    # no optimizations
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = 0
        j = 1
        out = 1
        stack = s[i]
        temp = 1
        while j < len(s):
            if s[j] in stack:
                i += 1
                j = i
                temp = 1
                stack = s[i]
            else:
                stack += s[j]
                temp += 1
            if temp > out:
                out = temp
            j += 1
            print("i: " + str(i))
            print("j: " + str(j))
            print("s: " + stack)
            print("o: " + str(out))
            print("t: " + str(temp))
            print("--------")
        return out

    # time complexity worst case: 0(n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        i = 0
        j = 0
        out = 0
        stack = {}
        temp = 0
        while j < len(s):
            if s[j] in stack:
                i = max(i, stack[s[j]])
            temp = j - i + 1
            stack[s[j]] = j + 1
            if temp > out:
                out = temp
            j += 1
        return out

# Tests


class TestSolution(unittest.TestCase):
    def test_1(self):
        print("test1")
        res = Solution().lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(res, 3)

    def test_2(self):
        print("test2")
        res = Solution().lengthOfLongestSubstring("bbbbb")
        self.assertEqual(res, 1)

    def test_3(self):
        print("test3")
        res = Solution().lengthOfLongestSubstring("pwwkew")
        self.assertEqual(res, 3)

    def test_4(self):
        print("test4")
        res = Solution().lengthOfLongestSubstring("aab")
        self.assertEqual(res, 2)

    def test_5(self):
        print("test5")
        res = Solution().lengthOfLongestSubstring("c")
        self.assertEqual(res, 1)

    def test_6(self):
        print("test6")
        res = Solution().lengthOfLongestSubstring("dvdf")
        self.assertEqual(res, 3)

    def test_7(self):
        print("test7")
        res = Solution().lengthOfLongestSubstring("")
        self.assertEqual(res, 0)

    def test_8(self):
        print("test8")
        res = Solution().lengthOfLongestSubstring("abba")
        self.assertEqual(res, 2)


if __name__ == '__main__':
    unittest.main()
