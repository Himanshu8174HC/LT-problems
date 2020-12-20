class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        d = Counter(chars)
        for i in words:
            count = Counter(i)
            for j in set(i):
                if j not in d:
                    break
                elif j in d and count[j]>d[j]:
                    break
            else:
                ans += len(i)
        return ans
