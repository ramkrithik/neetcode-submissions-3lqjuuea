class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        min_str,long_str = (str1,str2) if len(str1) < len(str2) else (str2,str1)

        prev = ""
        longest_divisor = [""]
        for i in min_str:
            prev+=i

            if min_str.replace(prev,"") == "" and long_str.replace(prev,"") == "":
                longest_divisor.append(prev)

        return longest_divisor[-1]