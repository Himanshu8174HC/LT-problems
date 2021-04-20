class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        
        
        root_val = max(nums)
        root_index = nums.index(root_val)
        root = TreeNode(root_val)
        
        root.left = self.constructMaximumBinaryTree(nums[:root_index])
        root.right = self.constructMaximumBinaryTree(nums[root_index+1:])
        
        return root
        
