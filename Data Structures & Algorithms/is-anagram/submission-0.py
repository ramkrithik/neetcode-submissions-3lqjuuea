class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for ch in s:
            if ch not in s_dict:
                s_dict[ch] = 0
            s_dict[ch] += 1
        t_dict = {}
        for ch in t:
            if ch not in t_dict:
                t_dict[ch] = 0
            t_dict[ch] += 1
        
        return s_dict == t_dict

        