class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:

        events = []
        for pos,r in lights:
            events.append((pos-r,1))
            events.append((pos+r+1,-1))
        
        events.sort()

        cursum = 0
        max_sum = 0
        max_pos = 0

        for pos,val in events:
            cursum += val
            if cursum>max_sum:
                max_pos = pos
                max_sum = cursum
        
        return max_pos


        # throws = []
        # for light in lights:
        #     throws.append((light[0]-light[1], light[0] + light[1]))
        
        # throws.sort()
        # illum = {}
        # max_illum = float("-inf")
        # max_illum_pos = throws[0][0]
        # print(throws)
        # for throw in throws:
        #     for j in range(throw[0],throw[1]+1):
        #         if j not in illum:
        #             illum[j] = 0
        #         illum[j]+=1

        #         if illum[j] > max_illum:
        #             max_illum = illum[j]
        #             max_illum_pos = j
        
        # return max_illum_pos

        