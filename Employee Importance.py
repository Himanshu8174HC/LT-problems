class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d = {}
        for e in employees:
            d[e.id] = e
        return self.helper(d, id)
        
    def helper(self, d, id):
        employee = d[id]
        total_importance = 0
        for i in employee.subordinates:
            total_importance += self.helper(d, i)
        return employee.importance + total_importance
        
