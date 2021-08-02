class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        temp = [0,0,0]
        for i, j, k in triplets:
            if i <= target[0] and j <= target[1] and k <= target[2]:
                temp = [max(temp[0], i), max(temp[1], j), max(temp[2], k)]
        return temp[0] == target[0] and temp[1] == target[1] and temp[2] == target[2]
        
