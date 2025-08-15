'''Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false'''







# My logic using recursive function

class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def search(r, c, idx, visited):
            if idx == len(word):
                return True
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx] or
                (r, c) in visited):
                return False

            visited.add((r, c))

            if (search(r+1, c, idx+1, visited) or
                search(r-1, c, idx+1, visited) or
                search(r, c+1, idx+1, visited) or
                search(r, c-1, idx+1, visited)):
                return True

            visited.remove((r, c))
            return False

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if search(r, c, 0, set()):
                        return True
        return False







# Leet code best logic

# class Solution(object):
#     def exist(self, board, word):
#         rows, cols = len(board), len(board[0])

#         # 1️⃣ Early prune: if board doesn't have enough letters
#         board_count = Counter(ch for row in board for ch in row)
#         word_count = Counter(word)
#         for ch, cnt in word_count.items():
#             if board_count[ch] < cnt:
#                 return False

#         # 2️⃣ Search from rarer starting letter
#         if board_count[word[0]] > board_count[word[-1]]:
#             word = word[::-1]

#         # 4️⃣ Start DFS from matching cells
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == word[0]:
#                     if len(word) == 1 or self.dfs(r, c, board, word, 0, {(r, c)}):
#                         return True
#         return False

#     def dfs(self, r, c, board, word, depth, visited):
#         if depth == len(word) - 1:  # matched the last char
#             return True

#         # explore neighbors
#         for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nr, nc = r + dr, c + dc
#             if (0 <= nr < len(board) and 0 <= nc < len(board[0]) and
#                 (nr, nc) not in visited and
#                 board[nr][nc] == word[depth + 1]):
                
#                 visited.add((nr, nc))
#                 if self.dfs(nr, nc, board, word, depth + 1, visited):
#                     return True
#                 visited.remove((nr, nc))

#         return False

