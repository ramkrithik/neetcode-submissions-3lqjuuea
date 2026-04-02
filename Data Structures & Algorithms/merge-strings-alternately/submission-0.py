class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        short, long = (word1,word2) if len(word1)< len(word2) else (word2, word1)

        new_s = ""
        for i in range(0,len(short)):
            new_s = f"{new_s}{word1[i]}{word2[i]}"
        if len(short) != len(long):
            new_s =f"{new_s}{long[i+1:]}"
        return new_s
        