# 1. Two Sum (https://leetcode.com/problems/two-sum/description/)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,n in enumerate(nums):
            if target-n in d:
                return [d[target-n], i]
            d[n] = i


# 9. Palindrome Number (https://leetcode.com/problems/palindrome-number/description/)
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


#21. Merge Two Sorted Lists (https://leetcode.com/problems/merge-two-sorted-lists/description/)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sortd_head = ListNode()
        sortd = sortd_head
        while list1 and list2:
            if list1.val < list2.val:
                sortd.next = list1
                list1 = list1.next
            else:
                sortd.next = list2
                list2 = list2.next
            sortd = sortd.next
        
        if list1:
            sortd.next = list1
        elif list2:
            sortd.next = list2
        return sortd_head.next


#26. Remove Duplicates from Sorted Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            k = 0
            seen = set()
            for i in range(len(nums)):
                if nums[i] not in seen:
                    nums[k] = nums[i]
                    seen.add(nums[i])
                    k+=1
            return k


#27. Remove Element (https://leetcode.com/problems/remove-element/description/)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k


#28. Find the Index of the First Occurrence in a String (https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = -1
        n_length = len(needle)
        length = len(haystack)
        for i in range(length):
            if haystack[i:i+n_length] == needle and index < 0:
                index = i
                break
        return index


#35. Search Insert Position (https://leetcode.com/problems/search-insert-position/description/)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
