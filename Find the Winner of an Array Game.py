########################################################### Time Limit Problem
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if max(arr)==arr[-1] and k > len(arr):
            return arr[-1]
        d = {}
        winner = 0
        while True:
            if arr[0]>arr[1]:
                winner = arr[0]
                arr.append(arr[1])
                arr.pop(1)
            else:
                winner = arr[1]
                arr.append(arr[0])
                arr.pop(0)
            if winner not in d:
                d[winner] = 1
                if d[winner] == k:
                    return winner
            else:
                d[winner] = d[winner]+1
                if d[winner] == k:
                    return winner
                    
 #################################################### No Time limit exceed                  
  current_num = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if current_num > arr[i]:
                count += 1
            else:
                current_num = arr[i]
                count = 1
            if count == k:
                    break

        return current_num
