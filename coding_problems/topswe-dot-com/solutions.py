"""
[1] 412. Fizz Buzz (https://leetcode.com/problems/fizz-buzz/)
"""
class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    arr = ["1"]
    for i in range(1,n):
      if (i+1)%5 == 0 and (i+1)%3 == 0:
        arr.append("FizzBuzz")
      elif (i+1)%3 == 0:
        arr.append("Fizz")
      elif (i+1)%5 == 0:
        arr.append("Buzz")
      else:
        arr.append(str(i+1))
    return arr


"""
[2] 1. Two Sum (https://leetcode.com/problems/two-sum/)
"""

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    d={}
    for i,n in enumerate(nums):
      dif = target-n
      if dif in d:
        return [d.get(dif), i]
      d[n] = i


"""
[3] 242. Valid Anagram (https://leetcode.com/problems/valid-anagram/)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))
    

"""
[4] 344. Reverse String (https://leetcode.com/problems/reverse-string/)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[len(s)-i-1] = s[len(s)-i-1],s[i]


"""
[5] 125. Valid Palindrome (https://leetcode.com/problems/valid-palindrome/)
"""

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('\W|_+','', s)
        return s == s[::-1]
    

"""
[6] 14. Longest Common Prefix (https://leetcode.com/problems/longest-common-prefix/)
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shrtr,lngr = min(strs), max(strs)
        res = ""
        for s,l in zip(shrtr,lngr):
            if s == l:
                res+=s
            else:
                break
        return res
    

"""
[7] 326. Power of Three (https://leetcode.com/problems/power-of-three/)
"""

import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        N=1
        while N<=n:
            if N==n:return True
            N=N*3
        return False