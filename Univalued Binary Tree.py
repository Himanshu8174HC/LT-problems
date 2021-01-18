class Solution(object):
    def isUnivalTree(self, root):
        if root is None :
            return True
        if root.left and root.val!= root.left.val:
            return False
        if root.right and root.val!= root.right.val:
            return False
        return self.isUnivalTree(root.right) and self.isUnivalTree(root.left)
