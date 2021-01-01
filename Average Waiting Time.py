class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        s = customers[0][0]
        t = s + customers[0][1]
        w = t - s
        
        for i in customers[1:]:
            s = i[0]
            if s <= t:
                t += i[1]
                w = w + t - s
            else:
                t = i[0]+i[1]
                w += i[1]
        return w/len(customers)
        
