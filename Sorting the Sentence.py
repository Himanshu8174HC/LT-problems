class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = sorted(s.split(), key = lambda a:a[-1])
        
        return ' '.join(i[:-1] for i in s)
