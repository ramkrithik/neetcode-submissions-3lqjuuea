class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)
        matchsticks.sort(reverse=True)

        if total %4 !=0:
            return False
        
        target = total//4
        sides = [0] * 4

        def dfs(i):
            
            if i>=len(matchsticks):
                return target == sides[0] == sides[1] == sides[2] == sides[3]
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= target:
                    sides[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[j] -= matchsticks[i]
                    
                    if sides[j] == 0:
                        break
            return False
        
        return dfs(0)

        