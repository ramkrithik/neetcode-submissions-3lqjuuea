class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque
        L = 0
        window = deque()
        max_window = 0

        for R in range(len(s)):
            
            if s[R] in window:
                while window:
                    val = window.popleft()
                    L+=1
                    if val == s[R]:
                        break
                    
            
            window.append(s[R])
            max_window = max(max_window, len(window))
        return max_window
