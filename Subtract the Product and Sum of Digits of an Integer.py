class Solution:
    def subtractProductAndSum(self, n: int) -> int:
      add = 0
      mul = 1
      n_temp = str(n)
      for i in n_temp:
        
        add += int(i)
        mul *= int(i)
        
      return mul - add
        
