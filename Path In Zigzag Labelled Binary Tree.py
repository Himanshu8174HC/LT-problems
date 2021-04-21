class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
      ans = []
      x = int(log(label, 2)) +1
      ans.append(label)
      while label >1:
        x -= 1
        
        temp = label//2
        end = (2 **x) - 1
        start = 2 **(x-1)
        diff = end - temp
        ans.append(start+diff)
        
        label = start + diff
      return ans[::-1]
