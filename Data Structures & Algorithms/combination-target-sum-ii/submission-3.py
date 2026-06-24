class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        unique = set()
        def build_combs(i, curr_list, curr_sum):
            if curr_sum == target:
                unique.add(tuple(curr_list.copy()))
                return

            if i >= len(candidates) or curr_sum>target:
                return
            curr_sum += candidates[i]
            curr_list.append(candidates[i])
            build_combs(i+1,curr_list,curr_sum)
            curr_list.pop()
            curr_sum -= candidates[i]

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                   i += 1
            build_combs(i+1,curr_list,curr_sum)
        
        build_combs(0,[],0)

        return [list(i) for i in unique]



