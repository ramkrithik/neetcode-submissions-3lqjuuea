class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        letter_count = Counter(t)
        curr_window = {}
        need = len(letter_count)
        have = set()
        min_len = float("inf")
        window = ()
        l = 0
        for r in range(len(s)):
            r_char = s[r]
            curr_window[r_char] = curr_window.get(r_char,0) + 1

            if r_char in letter_count and curr_window[r_char] >= letter_count[r_char]:
                have.add(r_char)
            
            while len(have) == need:
                if min_len > (r-l+1):
                    min_len = r-l+1
                    window = (l,r)
                
                curr_window[s[l]] -= 1

                if s[l] in letter_count and curr_window[s[l]] < letter_count[s[l]]:
                    have.remove(s[l])
                l+=1
        
        return "" if min_len == float("inf") else s[window[0]:window[1]+1]
            

        
        