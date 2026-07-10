class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        curr_min = arrays[0][0]
        curr_max = arrays[0][-1]
        res = 0

        for i in range(1,len(arrays)):
            res = max(res,abs(curr_min - arrays[i][-1]))
            res = max(res,abs(curr_max - arrays[i][0]))

            curr_min = min(arrays[i][0],curr_min)
            curr_max = max(arrays[i][-1],curr_max)
        
        return res


        
        