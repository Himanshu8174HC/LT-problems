class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        H = {}
        for i in range(len(list1)):
            H[list1[i]] = i
        ans = []
        score = 10000000
        for i in range(len(list2)):
            if list2[i] in H:
                cur = i + H[list2[i]]
                if cur < score:
                    ans = []
                    score = cur
                    ans.append(list2[i])
                elif cur == score:
                    ans.append(list2[i])
        return ans
