# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        NewRoot = None
        if t1 and t2:
            NewRoot = TreeNode(t1.val + t2.val)
            NewRoot.left = self.mergeTrees(t1.left, t2.left)
            NewRoot.right = self.mergeTrees(t1.right, t2.right)
            return NewRoot
        elif not t2 and t1:
            NewRoot = TreeNode(t1.val)
            NewRoot.left = self.mergeTrees(t1.left, None)
            NewRoot.right = self.mergeTrees(t1.right, None)
            return NewRoot
        elif not t1 and t2:
            NewRoot = TreeNode(t2.val)
            NewRoot.left = self.mergeTrees(None, t2.left)
            NewRoot.right = self.mergeTrees(None, t2.right)
            return NewRoot
        else:
            return None
            
###############################################################################
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
		    return t2
        elif not t2:
            return t1
    
	    
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
