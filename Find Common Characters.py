class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        d1 = Counter(A[0])
        for i in A[1:]:
            d2 = Counter(i)
            for k in d1:
                if k in d2:
                    d1[k] = min(d1[k], d2[k])
                else:
                    d1[k] = 0
        ans = []
        for k, v in d1.items():
            if v != 0:
                ans += [k]*v
        return ans
