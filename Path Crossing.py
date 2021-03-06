class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = {(0, 0)}
        location = [0, 0]
        for move in path:
            x, y = location
            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            elif move == 'W':
                x -= 1
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
                location = [x, y]
        return False
