class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        available = dict.fromkeys([20,10,5], 0)

        for _,i in enumerate(bills):
            print(available) 
            if _==0 and i!=5:
                return False
            
            elif i == 5:
                available[i] += 1
            
            else:
                amount_remaining = i-5
                for key in available:
                    if available[key] ==0 or key>amount_remaining:
                        continue
                    
                    bills_needed = amount_remaining//key

                    bills_used = min(bills_needed, available[key])
                    
                    amount_remaining -= bills_used*key
                    available[key] -= bills_used
                
                if amount_remaining != 0:
                    return False
                
                available[i] +=1
            

        
        return True
