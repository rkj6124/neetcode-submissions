class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                element = board[r][c]
                if element == ".":
                    continue
                if element in row_set[r] or element in col_set[c] or element in square_set[(r//3, c//3)]:
                    return False
                row_set[r].add(element)
                col_set[c].add(element)
                square_set[(r//3,c//3)].add(element)
        return True


