class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        ones = []
        
        for i, v in enumerate(arr):
            if v == 1:
                ones.append(i)
        
        if not ones:
            return [0, 2]
        elif len(ones) %3 !=0:
            return [ -1, -1]
        
        first = ones[0]
        second = ones[len(ones)//3]
        third = ones[len(ones)//3*2]
        
        length = len(arr) - third
        
        if arr[first:first+length] == arr[second:second+length] == arr[third:third+length]:
            return [first+length-1, second+length]
        return [-1, -1]
        
