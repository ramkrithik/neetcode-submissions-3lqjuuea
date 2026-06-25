class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        c = {}
        def dfs(i1,i2):

            if i2 == len(word2):
                return len(word1) - i1
            if i1 == len(word1):
                return len(word2) - i2
            
            if (i1,i2) in c:
                return c[(i1,i2)]

            #branch equals
            if word1[i1] == word2[i2]:
                c[(i1,i2)] = dfs(i1+1, i2+1)
            else:
                # branch delete 
                delete = dfs(i1+1,i2) + 1
                # branch replace
                replace = dfs(i1+1,i2+1) + 1
                
                # branch insert
                insert = dfs(i1,i2+1) + 1
                c[(i1,i2)] = min(delete, replace,insert)

            return c[(i1,i2)]
        
        return dfs(0,0)
            


        