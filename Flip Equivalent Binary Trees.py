class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
      
      def check(node1,node2):
        if not node1 and not node2:
          return True
        elif (not node1 and node2) or (node1 and not node2) or (node1.val!=node2.val):
          return False
        return (check(node1.left,node2.right) and check(node1.right,node2.left)) or (check(node1.left,node2.left) and check(node1.right,node2.right))
		
