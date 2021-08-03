class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        d = Counter(arr)
        
        d = dict(sorted(d.items(), key=lambda item: item[1]))
        ans = len(d)
        for i in d.values():
            k -= i
            
            if k < 0:
                break
            ans -= 1
        return ans
