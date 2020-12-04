####################################################################SET solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        SET = set()
        for i in s:
            if i  not in SET:
                SET.add(i)
            else:
                SET.remove(i)
                
        if len(SET) !=0:
            return len(s) - len(SET) +1
        else:
            return len(s)
            
            
######################################################################DICTIONARY solution
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
        odd = 0
        ret = 0
        for k in freq.keys():
            if freq[k] % 2 == 0:
                ret += freq[k]
            else:
                ret += freq[k] -1
                odd = 1
                
        return ret  + odd
