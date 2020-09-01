class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s,t=Counter(s),Counter(t)
        return sum([s[k]-t[k] for k in s if s[k]>t[k]])
