class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1d = {}
        for i in s1:
            if i not in s1d:
                s1d[i] = 0
            s1d[i] += 1
        
        k = len(s1)
        l = 0

        s2d = {}
        for r in range(len(s2)):
            
            if s2[r] not in s1:
                s2d = {}
                l=r+1
                continue
            char = s2[r]
            if char not in s2d:
                s2d[char] = 0
            s2d[char] += 1
            if (r-l+1) == k:
                if s2d == s1d:
                    return True
                s2d[s2[l]] -=1
                if s2d[s2[l]] == 0:
                    s2d.pop(s2[l])
                l+=1

        return False