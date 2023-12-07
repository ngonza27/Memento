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


"""
[14] 94. Binary Tree Inorder Traversal (https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1097355417/)
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        self.inorder(root, ans)
        return ans

    def inorder(self, node, ans):
        if node is None:
            return None
        self.inorder(node.left, ans)
        ans.append(node.val)
        self.inorder(node.right, ans)

"""
[15] 226. Invert Binary Tree (https://leetcode.com/problems/invert-binary-tree/description/)
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
"""
[16] 101. Symmetric Tree (https://leetcode.com/problems/symmetric-tree/description/)
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.hlp(root, root)

    def hlp(self, l, r):
        if not l and not r: return True
        if ((not l or not r) or l.val != r.val): return False
        return self.hlp(l.left, r.right) and self.hlp(l.right, r.left)
    
"""
[17] 104. Maximum Depth of Binary Tree (https://leetcode.com/problems/maximum-depth-of-binary-tree/)
"""

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))    

"""
[18] 100. Same Tree (https://leetcode.com/problems/same-tree/)
"""

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q): return False
        if not p and not q: return True
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(q.right, p.right)
    
"""
[19] 112. Path Sum (https://leetcode.com/problems/path-sum/)
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        itSums = False
        if not root: return False
        return self.sol(root, targetSum, 0, itSums)

    
    def sol(self, root, targetSum, val, itSums):
        if not root:
            return itSums
        root.val += val
        if root.val == targetSum and (not root.left) and (not root.right): 
            itSums = True
        itSums = self.sol(root.left, targetSum, root.val, itSums)
        itSums = self.sol(root.right, targetSum, root.val, itSums)
        return itSums
    
"""
[20] 111. Minimum Depth of Binary Tree (https://leetcode.com/problems/minimum-depth-of-binary-tree/)
"""

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if (not root.left) and (not root.right): 
            return 1
        if not root.left: 
            return 1 + self.minDepth(root.right)
        if not root.right: 
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        
"""
[21] 98. Validate Binary Search Tree (https://leetcode.com/problems/validate-binary-search-tree/)
"""

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    ans = []
    self.inorder(root, ans)
    return ans == sorted(ans) and len(ans) == len(set(ans))

  def inorder(self, root, ans):
    if not root: return None
    self.inorder(root.left, ans)
    ans.append(root.val)
    self.inorder(root.right, ans)

"""
[22] 206. Reverse Linked List (https://leetcode.com/problems/reverse-linked-list/)
"""

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    while head:
      ref = head.next
      head.next = prev
      prev = head
      head = ref
    return prev

"""
[23] 876. Middle of the Linked List (https://leetcode.com/problems/middle-of-the-linked-list/)
"""

class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    p1, p2 = head, head
    while p2 and p2.next:
      p1 = p1.next
      p2 = p2.next.next
    return p1

"""
[24] 102. Binary Tree Level Order Traversal (https://leetcode.com/problems/binary-tree-level-order-traversal/)
"""

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    lst = []
    stack = [root]
    while stack:
      temp = []
      lenn = len(stack)
      for _ in range(lenn):
        node = stack.pop(0)
        if node:
          temp.append(node.val)
          stack.append(node.left)
          stack.append(node.right)
      if temp:
        lst.append(temp)
    return lst
  
"""
[25] 1971. Find if Path Exists in Graph (https://leetcode.com/problems/find-if-path-exists-in-graph/)
"""

class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if (not edges) or source == destination: 
      return True  
        
    graph = defaultdict(list)  
    for pairs in edges: 
      graph[pairs[0]].append(pairs[1])
      graph[pairs[1]].append(pairs[0])

    queue = [source] 
    visited = {} 
    while queue: 
      last = queue.pop(0) 
      visited[last] = True 
      if last == destination: 
        return True 
      for node in graph[last]: 
        if node not in visited: 
          queue.append(node)
    return False

"""
[26] 200. Number of Islands (https://leetcode.com/problems/number-of-islands/)
"""

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid: 
      return 0
    rows, cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r, c):
      q = collections.deque()
      visit.add((r,c))
      q.append((r,c))
      while q:
        row, col = q.popleft()
        for row_offset, col_offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
          if (
              row + row_offset >= 0 and
              row + row_offset < rows and
              col + col_offset >= 0 and
              col + col_offset < cols and
              grid[row + row_offset][col + col_offset] == "1" and
              (row + row_offset, col + col_offset) not in visit
          ):
            q.append((row + row_offset, col + col_offset))
            visit.add((row + row_offset, col + col_offset))


    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == "1" and (r, c) not in visit:
          bfs(r,c)
          islands += 1
    return islands

"""
[27] 695. Max Area of Island (https://leetcode.com/problems/max-area-of-island/)
"""

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    if not grid: 
      return 0
    rows, cols = len(grid), len(grid[0])
    visit = set()
    max_area = 0

    def bfs(r, c):
      q = collections.deque()
      sizes = 1
      visit.add((r,c))
      q.append((r,c))
      while q:
        row, col = q.popleft()
        for row_offset, col_offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
          if (
              row + row_offset >= 0 and
              row + row_offset < rows and
              col + col_offset >= 0 and
              col + col_offset < cols and
              grid[row + row_offset][col + col_offset] == 1 and
              (row + row_offset, col + col_offset) not in visit
          ):
            q.append((row + row_offset, col + col_offset))
            visit.add((row + row_offset, col + col_offset))
            sizes += 1
      return sizes

    for r in range(rows):
      for c in range(cols):
        if grid[r][c] == 1 and (r, c) not in visit:
          l = bfs(r,c)
          if l > max_area:
            max_area = l 
    return max_area
  
"""
[28] 1905. Count Sub Islands (https://leetcode.com/problems/count-sub-islands/)
"""

class Solution:
  def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    if not grid1 and not grid2: 
      return 0
    rows, cols = len(grid1), len(grid1[0])
    islands = 0

    def bfs(r, c):
      f = 1
      q = collections.deque()
      q.append((r,c))
      while q:
        row, col = q.popleft()
        if grid2[row][col] == 0: 
          continue
        grid2[row][col] = 0
        if grid1[row][col] == 0:
          f = 0
        for row_offset, col_offset in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
          if (
              row + row_offset >= 0 and row + row_offset < rows and
              col + col_offset >= 0 and col + col_offset < cols and
              grid2[row + row_offset][col + col_offset] == 1):
            q.append((row + row_offset, col + col_offset))
      return f

    for r in range(rows):
      for c in range(cols):
        if grid2[r][c]:
          f = bfs(r,c)
          if f: islands += 1
    return islands

"""
[29] 20. Valid Parentheses (https://leetcode.com/problems/valid-parentheses/)
"""

class Solution:
  def isValid(self, s: str) -> bool:
    d = {"}": "{", "]": "[", ")": "("}
    if len(s) < 2 or len(s)%2 != 0 or s[0] in d.keys():
      return False
    q = collections.deque()
    for p in s:
      if p in d.values():
        q.append(p)
      elif len(q) and d.get(p) == q[-1]:
        q.pop()
      else:
        return False
    return len(q) == 0