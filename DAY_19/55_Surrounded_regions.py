'''You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.
Example 2:
Input: board = [["X"]]
Output: [["X"]]'''







# My logic using for loop and condition only

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])

        for j in range(n):
            if board[0][j] == "O":
                board[0][j] = "S"
            if m > 1 and board[m-1][j] == "O":
                board[m-1][j] = "S"
        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "S"
            if n > 1 and board[i][n-1] == "O":
                board[i][n-1] = "S"

        changed = True
        while changed:
            changed = False
            for i in range(1, m-1):
                for j in range(1, n-1):
                    if board[i][j] == "O":
                        if (board[i-1][j] == "S" or
                            board[i+1][j] == "S" or
                            board[i][j-1] == "S" or
                            board[i][j+1] == "S"):
                            board[i][j] = "S"
                            changed = True

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "S":
                    board[i][j] = "O"

                






# Leet code best logic 

# class Solution:
#     def solve(self, gd):
#         rc, cc = len(gd), len(gd[0])

#         def wave(r0, c0):
#             if gd[r0][c0] != 'O': return

#             st = [(r0, c0)]

#             while st:
#                 r, c = st.pop()
#                 gd[r][c] = 'U'
#                 for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#                     r2, c2 = r + dr, c + dc
#                     if r2 < 0 or r2 == rc or c2 < 0 or c2 == cc or gd[r2][c2] != 'O': continue
#                     st.append((r2, c2))

#         def main():
#             for r in range(rc):
#                 wave(r, 0)
#                 wave(r, cc - 1)

#             for c in range(cc):
#                 wave(0, c)
#                 wave(rc - 1, c)

#             for r in range(rc):
#                 for c in range(cc):
#                     if gd[r][c] == 'O':
#                         gd[r][c] = 'X'
#                     elif gd[r][c] == 'U':
#                         gd[r][c] = 'O'

#         main()