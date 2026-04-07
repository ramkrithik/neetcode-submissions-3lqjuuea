class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            day, curr_cap = 1, cap
            for w in weights:
                if curr_cap -w <0:
                    day+=1
                    if day > days:
                        return False
                    curr_cap = cap
                curr_cap -= w
            return True
        while l<=r:
            m = (l+r)//2
            if canShip(m):
                res = min(res,m)
                r = m-1
            else:
                l=m+1
        return res
        