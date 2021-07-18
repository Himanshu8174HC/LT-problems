class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people = sorted(people, reverse = True)
        
        temp1 = 0
        temp2 = len(people)-1
        ans = 0
        
        while temp1 < temp2:
            if people[temp1]+people[temp2] <= limit:
                temp2 -=1
            temp1 += 1
            ans += 1
        if temp1 == temp2:
            ans +=1
        return ans
            
                
                
            
            
     
