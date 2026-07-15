class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        start_indices = []

        for r in range(0,len(board)):
            for c in range(0,len(board[0])):
                if board[r][c] == word[0]:
                    start_indices.append((r,c))
        
        if not start_indices:
            return False
        
        visited = set()
        def dfs(r,c,word_len):
            if board[r][c] != word[word_len]:
                return False
            if word_len == len(word)-1:
                return True
            
            visited.add((r, c))

            movement = [(1,0),(0,1),(-1,0),(0,-1)]

            for _r,_c in movement:
                new_r = r+_r
                new_c = c+_c
                if new_r >= len(board) or new_c >= len(board[0]) or (min(new_r,new_c) < 0) or (new_r,new_c) in visited:
                    continue
                else:
                    if dfs(new_r,new_c,word_len+1):
                        return True
            visited.remove((r, c))
            return False
        
        for coor in start_indices:
            if dfs(coor[0],coor[1],0):
                return True
            visited = set()
        
        return False


        