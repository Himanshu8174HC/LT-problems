class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        
        def post(root):
            for child in root.children:
                post(child)
            res.append(root.val)
        
        res = []
        post(root)
        return res
        
        
