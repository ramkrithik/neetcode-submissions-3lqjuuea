class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        original_color = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        def dfs(r,c,visited):
            
            if min(r,c) <0 or r == rows or c == cols or (r,c) in visited or image[r][c]!=original_color:
                return
            
            visited.add((r,c))
            image[r][c] = color

            dfs(r+1,c,visited)
            dfs(r-1,c,visited)
            dfs(r,c+1,visited)
            dfs(r,c-1,visited)
            
            return 
        
        dfs(sr,sc,set())
        return image
