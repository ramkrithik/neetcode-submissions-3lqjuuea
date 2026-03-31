class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str_1 = strs[0]
        lcp = ""
        for i in range(0, len(str_1)):
            for j in range(1,len(strs)):
                if len(strs[j]) <= i:
                    return lcp
                if strs[j][i] != str_1[i]:
                    return lcp
            lcp += str_1[i]
        return lcp

        