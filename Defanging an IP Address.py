###########################1st
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
        
        
#####################2nd
class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=list(address)
        for i in range(len(a)):
             if a[i]== ".":
                    a[i]= "[.]"
                    
                    
        return ("".join(a))
