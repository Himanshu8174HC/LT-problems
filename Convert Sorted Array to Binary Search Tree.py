class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return helper(nums, 0 ,len(nums)-1)
def helper(nums, start, end):
    if start >end:
        return
    mid = (start+end)//2
    root = TreeNode(nums[mid])
    root.left = helper(nums,start, mid-1)
    root.right = helper(nums,mid+1, end)
    return root
