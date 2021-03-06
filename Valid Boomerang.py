class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points
        ab = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**(0.5)
        bc = ((b[0] - c[0])**2 + (b[1] - c[1])**2)**(0.5)
        ac = ((a[0] - c[0])**2 + (a[1] - c[1])**2)**(0.5)
        if (ab == bc + ac) or (bc == ab + ac) or (ac == ab + bc):
            return False
        return True
