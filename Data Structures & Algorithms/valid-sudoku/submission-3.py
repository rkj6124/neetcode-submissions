class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                box_id = (r//3)*3 + (c//3)
                if element in rows[r] or element in cols[c] or element in squares[box_id]:
                    return False
                rows[r].add(element)
                cols[c].add(element)
                squares[box_id].add(element)
        return True


