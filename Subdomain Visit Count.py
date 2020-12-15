class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = {}
        for c in cpdomains:
            s = c.replace('.',' ').split()
            n = int(s[0])
            for i in range(len(s)-1,0,-1):
                print(s[i])
                t = ".".join(s[i:])
                if t in d:
                    d[t] = d[t] + n  
                else:
                    d[t] = n
        return [str(d[i])+" "+ i for i in d]
		
        
