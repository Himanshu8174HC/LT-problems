class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
      temp1 = []
      if x == 1:
        temp1 = [1]
      else:
        x_ = 1
        while x_ < bound:
          temp1.append(x_)
          x_ *= x
          
      temp2 = []
      if y == 1:
        temp2 = [1]
      else:
        y_ = 1
        while y_ < bound:
          temp2.append(y_)
          y_ *= y
          
      s = set()
      for i in temp1:
        for j in temp2:
          if i + j <= bound:
            s.add(i+j)
      return s
        
        
