class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        sets = set()

        for i in mat:
            if len(sets) == 0:
                sets = set(i)
            else:
                sets = sets.intersection(i)
        
        return min(sets) if len(sets)>0 else -1
        