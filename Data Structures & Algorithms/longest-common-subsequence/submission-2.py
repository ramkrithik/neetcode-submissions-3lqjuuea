class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        c = {}
        def dfs(i1, i2):
            if i1 == len(text1) or i2 == len(text2):
                return 0
            
            if (i1,i2) in c:
                return c[(i1,i2)]
            
            if text1[i1] == text2[i2]:
                c[(i1,i2)] = 1 + dfs(i1+1,i2+1)
            else:
                c[(i1,i2)] = max(dfs(i1+1,i2), dfs(i1,i2+1))
            
            return c[(i1,i2)]
        
        return dfs(0,0)
            



        # m = len(text1)
        # n = len(text2)
        # matrix = [[0]*n for i in range(m)]

        # for i in range(m):
        #     for j in range(n):

        #         if i-1 < 0:
        #             matrix[i][j] = max(matrix[i][j-1],matrix[i][j])
        #         elif j-1<0:
        #             matrix[i][j] = max(matrix[i][j],matrix[i-1][j])
        #         else:
        #             matrix[i][j] = max(matrix[i][j-1],matrix[i-1][j])

        #         if text1[i] == text2[j]:
        #             diag = matrix[i-1][j-1] if i-1>=0 and j-1>=0 else 0
        #             matrix[i][j] = max(matrix[i][j], diag + 1)
        # return matrix[-1][-1]