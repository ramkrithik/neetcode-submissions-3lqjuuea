class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        freq = {}
        max_size = float("-inf")
        res = 0

        for R in range(len(s)):

            freq[s[R]] = freq.get(s[R],0) + 1

            max_size = max(max_size, freq[s[R]])

            while (R-L+1) - max_size > k:
                freq[s[L]] -=1
                L+=1
            
            res = max(res, (R-L+1))
        
        return res
            


        