class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif s == "":
            return True

        i1 = 0

        for i2 in range(len(t)):
            if t[i2] == s[i1]:
                i1+=1
            if i1 == len(s):
                break
        
        return i1 == len(s)