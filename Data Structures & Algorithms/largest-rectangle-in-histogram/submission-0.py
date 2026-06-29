class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for idx, height in enumerate(heights):
            stack_idx = idx
            while stack and stack[-1][1]>height:
                stack_idx, stack_h = stack.pop()
                curr_area = (idx-stack_idx) * stack_h
                max_area = max(max_area, curr_area)
            stack.append((stack_idx, height))
        
        n = len(heights)
        while stack:
            idx, h = stack.pop()
            curr_area = (n-idx) * h
            max_area = max(max_area,curr_area)
        
        return max_area


        