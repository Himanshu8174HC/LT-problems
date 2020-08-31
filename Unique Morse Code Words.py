class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        CODE = {'a': '.-',   'b': '-...',  'c': '-.-.',  'd': '-..',   'e': '.',    'f': '..-.',
                'g': '--.',  'h': '....',  'i': '..',    'j': '.---',  'k': '-.-',   'l': '.-..',
                'm': '--',   'n': '-.',    'o': '---',   'p': '.--.',  'q': '--.-',  'r': '.-.',
                's': '...',  't': '-',     'u': '..-',   'v': '...-',  'w': '.--',   'x': '-..-',
                'y': '-.--', 'z': '--..',
                
                }
        s=[]
        for xi in words:
            ans = ""
            for word in xi:
                ans= ans + CODE.get(word)
            s.append(ans)
        return len(set(s))
