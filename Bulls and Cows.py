class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        myCount=collections.Counter()
        temp = set()
        wrong = 0
        right = 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                temp.add(i)
                right += 1
            else:
                myCount[secret[i]] +=1
                    
        for i in range(len(guess)):
            if i not in temp and myCount[guess[i]] >0:
                wrong +=1
                myCount[guess[i]] -=1
                
        return str(right) +"A" + str(wrong) + "B"
