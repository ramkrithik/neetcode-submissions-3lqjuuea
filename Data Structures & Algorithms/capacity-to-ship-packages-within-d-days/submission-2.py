class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights) # 10, 26
        res = r

        def canShip(cap):
            day, curr_cap = 1, cap
            for w in weights: 
                # 16,12,6,5,2,
                # 11,7,1,0
                if curr_cap -w <0:
                    day+=1
                    if day > days:
                        return False
                    curr_cap = cap
                curr_cap -= w
            return True

        while l<=r:
            m = (l+r)//2 #18, 13
            if canShip(m):
                res = min(res,m)
                r = m-1
            else:
                l=m+1
        return res
        