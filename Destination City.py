class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        city = set()
        for i in paths:
            s.add(i[0])
            city.add(i[0])
            city.add(i[1])
        return (city - s).pop()
            
