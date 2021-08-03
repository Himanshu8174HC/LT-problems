class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        while c:
            s = min(c.keys())
            for i in range(s, s + k):
                if i in c:
                    c[i] -= 1
                    if c[i] == 0:
                        c.pop(i)
                else:
                    return False
        return True
        
