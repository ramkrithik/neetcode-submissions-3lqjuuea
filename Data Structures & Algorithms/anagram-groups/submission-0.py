class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        has = {}
        for s in strs:
            d = {}
            for char in s:
                if char not in d:
                    d[char] = 0
                d[char] += 1
            encoded = ""
            for i in sorted(d.keys()):
                encoded += f"{i}{d[i]}"
            if encoded not in has:
                has[encoded] = []
            has[encoded].append(s)
        return list(has.values())
        