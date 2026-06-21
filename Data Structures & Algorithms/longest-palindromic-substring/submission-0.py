class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = float("-inf")
        max_len_idx = None
        for i in range(0, len(s)):
            l,r = i,i

            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1) > max_len:
                    max_len = (r-l+1)
                    max_len_idx =[l,r]
                l-=1
                r+=1
            
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>max_len:
                    max_len = (r-l+1)
                    max_len_idx =[l,r]
                l-=1
                r+=1
        
        return s[max_len_idx[0]:max_len_idx[1]+1]

        