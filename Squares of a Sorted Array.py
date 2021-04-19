class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = []
        ans = []
        for i in nums:
            if i < 0:
                stack.append(-i)
            else:
                while stack and stack[-1] < i:
                    ans.append(stack.pop() ** 2)
                ans.append(i ** 2)
        while stack:
            ans.append(stack.pop() ** 2)
        return ans
