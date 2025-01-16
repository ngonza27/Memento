# 1. Two Sum (https://leetcode.com/problems/two-sum/description/)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            if target-n in d:
                return [d[target-n], i]
            d[n] = i


# 9. Palindrome Number (https://leetcode.com/problems/palindrome-number/)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)


#13. Roman to Integer (https://leetcode.com/problems/roman-to-integer/description/)
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        d = {
            "I" : 1,"V" : 5,"X" : 10,"L" : 50, "C" : 100,"D" : 500,"M" : 1000,
            "IV" : 4, "IX" : 9,"XL" : 40,"XC" : 90,"CD" : 400,"CM" : 900,
        }
        while i < len(s):
            doubl = s[i:i+2]
            if doubl in d and len(doubl) > 1:
                res += d[doubl]
                i+=2
            else:
                res += d[s[i]]
                i+=1
        return res


# 14. Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/description/)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        mns = strs[0]
        mxs = strs[-1]
        res = ""
        for i in range(len(mns)):
            if mns[i] != mxs[i]:
                break
            res = res + mns[i]
        return res


# 20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/description/)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {')': '(', '}': '{', ']': '['}
        if len(s)%2 != 0: return False        
        for c in s:
            if c in close and len(stack) and stack[-1] == close[c]:
                stack.pop()
            else:
                stack.append(c)
        return not bool(len(stack))
