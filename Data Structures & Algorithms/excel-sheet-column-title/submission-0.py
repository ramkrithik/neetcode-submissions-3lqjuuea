class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        col = ""
        while columnNumber>0:
            columnNumber -=1
            col = chr(ord("A") + (columnNumber%26)) + col
            columnNumber = columnNumber//26
            
        return col