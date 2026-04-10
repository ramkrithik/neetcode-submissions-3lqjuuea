class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        max_len = 0
        for i in words:
            max_len = max(max_len,len(i))
        
        if max_len != len(words):
            return False
        
        for i in range(0,len(words)):
            if len(words[i]) < max_len:
                words[i] = words[i] + " "*(max_len-len(words[i]))
        
        for i in range(1, max_len):
            for j in range(i-1,-1,-1):
                if words[i][j]!=words[j][i]:
                    return False
        return True
            