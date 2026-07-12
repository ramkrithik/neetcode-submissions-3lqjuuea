class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        
        for asteroid in asteroids:

            if not stack:
                stack.append(asteroid)
                continue
            while stack and asteroid < 0 < stack[-1]:
                if abs(stack[-1]) > abs(asteroid):
                    break
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroid)
        
        return stack
                    
                    
                    