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
