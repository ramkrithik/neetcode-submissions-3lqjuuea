class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitmap = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if digits == "":
            return []

        cur_comb, all_comb = "",[]
        self.helper(0,cur_comb,all_comb,digits,digitmap)

        return all_comb

    
    def helper(self,i,cur_comb,all_comb,digits,digitmap):

        if len(cur_comb) == len(digits):
            all_comb.append(cur_comb)
            return
        if i >= len(digits):
            return
        
        for j in digitmap[digits[i]]:
            self.helper(i+1,cur_comb+j,all_comb,digits,digitmap)
    

        