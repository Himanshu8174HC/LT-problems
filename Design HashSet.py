class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d =[]

    def add(self, key: int) -> None:
        self.d.append(key)
        
        

    def remove(self, key: int) -> None:
        self.l = []
        for i in self.d:
            if i!= key:
                self.l.append(i)
        self.d = self.l
                
            
        
        
        
        

    def contains(self, key: int) -> bool:
        if key in self.d:
            return True
        else:
            return False
        """
        Returns true if this set contains the specified element
        """
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
