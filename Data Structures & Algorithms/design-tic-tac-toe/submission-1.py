class TicTacToe:

    def __init__(self, n: int):

        self.n = n
        self.matrix = [[0] * n for i in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:

        self.matrix[row][col] = player

        c_s = 0
        for c in range(0,self.n):
            c_s += 1 if self.matrix[row][c] == player else 0
        
        c_s_bool = c_s == self.n
        
        r_s = 0
        for r in range(0,self.n):
            r_s += 1 if self.matrix[r][col] == player else 0
        r_s_bool = r_s == self.n
        

        diag_l = 0
        for i in range(0,self.n):
            diag_l += 1 if self.matrix[i][i] == player else 0
        diag_l_bool = diag_l == self.n
        
        diag_r = 0
        for i,j in enumerate(range(self.n-1,-1,-1)):
            diag_r += 1 if self.matrix[i][j] == player else 0
        diag_r_bool = diag_r == self.n
        
        
        return player if c_s_bool or r_s_bool or diag_l_bool or diag_r_bool else 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
