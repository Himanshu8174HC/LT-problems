1st############################################################
if high%2==0 and low%2==0:
            return ((high-low)//2)
        elif high%2!=0 and low%2!=0:
            return ((high-low)//2)+1
        else:
            return ((high-low)//2)+1
            
            
            
2nd############################################################
ans=0
        if low%2==1 or high%2==1:
            ans+=1
        return ((high-low)//2)+ans
        
 
