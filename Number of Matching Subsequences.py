class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        matches = 0
        for word in words:
            start = 0
            found = True
            for char in word:
                location = s.find(char, start)
                if location == -1:
                    found = False
                    break
                start = location + 1
            if found:
                matches += 1
        return matches
