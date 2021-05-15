class Solution:
    def flatten(self, root: TreeNode) -> None:
      pre = None
        
      def helper( node):
        if node:
          helper( node.right )
          helper( node.left )

                
          nonlocal pre
          node.right = pre
          node.left = None
          pre = node
                
        
        
      helper(root)
      
