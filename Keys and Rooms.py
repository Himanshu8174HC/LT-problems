class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        stack = [0]
        
        while stack:
            r = stack.pop()
            seen.add(r)
            
            for i in rooms[r]:
                if i not in seen:
                    stack.append(i)
        return len(seen) == len(rooms)
        
