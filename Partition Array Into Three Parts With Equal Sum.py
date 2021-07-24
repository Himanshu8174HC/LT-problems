class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
        s = sum(arr) / 3
        
        if s != int(s) and len(arr) < 3:
            return False
        
        index = 0
        temp = 0
        
        for i in range(len(arr)-1):
            temp += arr[i]
            
            if index == 2:
                break
           
            if temp == s:
                index += 1
                temp = 0
                
        return index == 2
        
