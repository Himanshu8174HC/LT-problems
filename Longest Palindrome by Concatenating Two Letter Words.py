class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
    
        d = collections.Counter(words)
        
        same = 0
        mid = 0
        diff = 0
        for k, v in d.items():
            if k[0] == k[1]:
                same += v //2 *4
                
                if v %2 ==1:
                    mid = 2
            else:
                diff += min(d[k], d[k[::-1]]) *2
        return same + mid + diff
                
            
                
            
        
