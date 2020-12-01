class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1] > nums[i] and len(stack) + len(nums)-i > k: # {len(stack) + len(nums)-i > k} => if we add element in stack and enough elemnt in the remaining element in the array is greator than k then we we keep poping
                stack.pop() #pop stack only if array have enugh element
            if len(stack)< k:
                stack.append(nums[i])
        return stack
