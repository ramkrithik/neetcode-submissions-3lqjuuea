class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if s == t:
            return 0
        elif t == "":
            return 0
        
        
        i1 = 0

        for i in range(len(s)):
            if s[i] == t[i1]:
                i1+=1
            
            if i1 == len(t):
                return 0

        return len(t) - i1


