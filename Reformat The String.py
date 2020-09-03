class Solution:
    def reformat(self, s: str) -> str:
        num = []
        alp = []
        for ch in s:
            if ch.isalpha():
                num.append(ch)
            else:
                alp.append(ch)
        
        n = len(num)
        m = len(alp)
        
        # make sure n > m
        if n < m:
            n, m = m, n
            num, alp = alp, num
            
        if n-m > 1:
            return ''
        
        i,j = 0, 0
        res = []
        while i < n and j < m:
            res.append(num[i])
            res.append(alp[j])
            i += 1
            j += 1
        
        if n > m:
            res.append(num[i])
        
            
        return ''.join(res)
