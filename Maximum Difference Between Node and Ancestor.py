class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        def help(root,maxx,minn):
            if not root:
                return abs(maxx-minn)
            if root.val>=maxx:
                maxx = root.val
            if root.val<=minn:
                minn = root.val
            return max(help(root.left,maxx,minn), help(root.right,maxx,minn), abs(maxx-minn))
        return help(root,-100000,100000)
            
            
