class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local,domain = email.split('@')
            tmp = ""
            for c in local:
                if c==".":
                    continue
                elif c=="+":
                    break
                else:
                    tmp += c
            ans.add(tmp+"@"+domain)
    
        return len(ans)
        
