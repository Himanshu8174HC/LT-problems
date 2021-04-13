class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.ans = []
        self.flatten(nestedList)
        
    def flatten(self, lst):
        for i in lst:
            if i.isInteger():
                self.ans.append(i.getInteger())
            else:
                self.flatten(i.getList())
    
    def hasNext(self) -> bool:
        return len(self.ans)
    
    def next(self) -> int:
        return self.ans.pop(0)
    
