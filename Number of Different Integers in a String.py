class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        a = set()
        temp = ""
        for i in word:
            if i.isdigit():
                temp+=i
            if i.isalpha() and len(temp)!=0:
                a.add(int(temp))
                temp= ""
            continue
        if len(temp)!=0:
            a.add(int(temp))
        return len(a)
                
                
