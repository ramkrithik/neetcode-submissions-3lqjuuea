class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        c = {}

        def dfs(i):
            if i==len(s):
                return True
            
            if i in c:
                return c[i]
            
            for word in wordDict:
                if s[i: i+len(word)] == word:
                    if dfs(i+len(word)):
                        c[i]=True
                        return True
            c[i] = False
            return c[i]
        
        return dfs(0)
                    

        # def dfs(curr_words):
        #     joined = "".join(curr_words)

        #     if len(joined) > len(s):
        #         return False
            
        #     if len(joined) == len(s):
        #         if s == joined:
        #             return True
        #         else:
        #             return False
            
        #     for word in wordDict:
        #         curr_words.append(word)
        #         if dfs(curr_words):
        #             return True
        #         curr_words.pop()
            
        #     return False
        
        # return dfs([])
        