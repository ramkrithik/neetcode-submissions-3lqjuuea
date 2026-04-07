class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[0] <= target and target <=i[-1]:
                l,r = 0, len(i)-1
                while l<=r:
                    m = (l+r)//2
                    if i[m] == target:
                        return True
                    if i[m] < target:
                        l = m+1
                    else:
                        r = m-1
        return False
