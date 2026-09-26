class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row - O(n^2)
        for row in board:
            seen = {str(key): False for key in range(1, 10)}
            for num in row:
                if num == ".": continue
                if seen[num]: return False
                seen[num] = True

        # check each column - O(n^2)
        for c in range(len(board[0])):
            seen = {str(key): False for key in range(1, 10)}
            for row in board:
                num = row[c] 
                if num == ".": continue
                if seen[num]: return False
                seen[num] = True

        # check each 3x3 - O(n^2)
        for t in range(0, 9, 3):
            for l in range(0, 9, 3):
                # board[t][l] is the top left
                seen = {str(key): False for key in range(1, 10)}
                for r in range(t,t+3):
                    for c in range(l,l+3):
                        num = board[r][c]
                        if num == ".": continue
                        if seen[num]: return False
                        seen[num] = True
        
        return True

