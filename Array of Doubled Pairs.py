arr = sorted(arr, key = abs)
        d = Counter(arr)
        
        for i in arr:
            while d[i] > 0 and d[2*i] > 0:
                d[i] -= 1
                d[2*i] -= 1
        
        for v in d.values():
            if v >= 1:
                return False
        return True
        
