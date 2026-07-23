class Solution:
    def customSortString(self, order: str, s: str) -> str:

        s = list(s)
        shift = 0
        for op in order:
            for i in range(shift,len(s)):
                if s[i] == op:
                    s[shift],s[i] = s[i], s[shift]
                    shift +=1
        
        return "".join(s)