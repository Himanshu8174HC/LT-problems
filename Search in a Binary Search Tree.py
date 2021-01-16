###################################################3RECURSIVE SOLUTION
class Solution(object):
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)
        
##################################################ITERATIVE SOLUTION
class Solution(object):
    def searchBST(self, root, val):
        while root and val != root.val:
            root = root.left if val < root.val else root.right
        return root
