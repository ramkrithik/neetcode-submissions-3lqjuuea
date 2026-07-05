class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        new_num = n
        while True:
            s = 0
            for i in str(new_num):
                s += int(i) ** 2
            
            if s == 1:
                return True
            elif s in seen:
                return False
            else:
                new_num = s
                seen.add(s)
        