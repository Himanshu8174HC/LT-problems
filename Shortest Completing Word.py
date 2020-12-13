class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        temp1 = temp2 = ""
        valid = []
        stats = True
        for letter in licensePlate:
            if letter.isalpha():
                temp1 += letter.lower()
                
        for word in words:
            temp2 = word
            for l in temp1:
                if l in temp2:
                    temp2 = temp2.replace(l,"",1)
                else:
                    stats = False
                    break
            if stats:
                valid.append(word)
            else:
                stats = True
		
        valid = sorted(valid, key=len)
        return valid[0]
