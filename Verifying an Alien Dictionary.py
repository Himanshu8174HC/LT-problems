class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d1 = {}
        
        for i in range(len(order)):
            d1[order[i]] = i
            
        temp1 = []
        temp2 = []
        
        for char in words:
            for j in range(len(char)):
                temp1.append(d1[char[j]])
            
            temp2.append(temp1)
            temp1 =[]
        
        for i in range(len(words)-1):
            
            
            if temp2[i] > temp2[i+1]:
                
                
                return False
        
        
        return True
