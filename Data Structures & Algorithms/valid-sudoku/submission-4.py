class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue

                box_id = (r//3)*3+(c//3)
                mask = 1 << int(board[r][c])

                if rows[r] & mask > 0 or cols[c] & mask > 0 or squares[box_id] & mask > 0:
                    return False

                rows[r] |= mask
                cols[c] |= mask
                squares[box_id] |= mask 
        
        return True


