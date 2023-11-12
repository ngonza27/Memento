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
    

"""
[8] 191. Number of 1 Bits (https://leetcode.com/problems/number-of-1-bits/)
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
    

"""
[9] 303. Range Sum Query - Immutable (https://leetcode.com/problems/range-sum-query-immutable/)
"""

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


"""
[10] 509. Fibonacci Number (https://leetcode.com/problems/fibonacci-number/)
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
    

"""
[11] 70. Climbing Stairs (https://leetcode.com/problems/climbing-stairs/)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for _ in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one

"""
[12] 746. Min Cost Climbing Stairs (https://leetcode.com/problems/min-cost-climbing-stairs/description/)
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
           cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
    


"""
[13] 121. Best Time to Buy and Sell Stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit=0, 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[buy]:
                buy = i
                sell = i
            if i > buy:
                sell = i
                profit = max(profit,prices[sell]-prices[buy])
        return profit