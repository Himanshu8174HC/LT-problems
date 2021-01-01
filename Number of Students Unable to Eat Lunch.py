class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        d = Counter(students)
        for j in sandwiches:
            if d[j]>0:
                d[j]-=1
            else:
                break
        return d[0]+d[1]
        
        
