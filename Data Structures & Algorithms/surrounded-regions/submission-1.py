class Solution:
    def solve(self, board: List[List[str]]) -> None:

        connected_to_edge = set()

        def dfs(r,c):
            
            if board[r][c] == "X":
                return
            
            connected_to_edge.add((r,c))

            movements = [(0,1),(1,0),(0,-1),(-1,0)]

            for movement in movements:
                new_r = r+movement[0]
                new_c = c+movement[1]
                if min(new_r,new_c) < 0 or new_r>=len(board) or new_c>=len(board[0]) or (new_r,new_c) in connected_to_edge:
                    continue
                
                dfs(new_r,new_c)
            
            return



        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                
                if (min(i,j) == 0 or i == len(board)-1 or j==len(board[0])-1) and board[i][j]=="O":
                    dfs(i,j)
        
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if (i,j) not in connected_to_edge:
                    board[i][j] = "X"
                
