class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        csp=word.capitalize()
        allow=word.lower()
        upp=word.upper()
        if csp==word or allow==word or upp==word:
            return True
        return False
