from collections import Counter


class Solution:

  def exist(self, board: list[list[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])

    # --- Search Pruning 1: Character Frequency Check ---
    board_counts = Counter(char for row in board for char in row)
    word_counts = Counter(word)

    for char, count in word_counts.items():
      if board_counts[char] < count:
        return False  # Not enough characters in grid to form word

    # --- Search Pruning 2: Reverse Search Direction ---
    # Start searching from whichever end of the word appears LEAST frequently
    if board_counts[word[0]] > board_counts[word[-1]]:
      word = word[::-1]

    # --- DFS Backtracking ---
    def dfs(r: int, c: int, index: int) -> bool:
      if index == len(word):
        return True

      if (
          r < 0
          or r >= ROWS
          or c < 0
          or c >= COLS
          or board[r][c] != word[index]
      ):
        return False

      # In-place marking to track visited cells without extra memory
      temp = board[r][c]
      board[r][c] = "#"

      # Explore 4 orthogonal directions
      found = (
          dfs(r + 1, c, index + 1)
          or dfs(r - 1, c, index + 1)
          or dfs(r, c + 1, index + 1)
          or dfs(r, c - 1, index + 1)
      )

      # Backtrack: restore cell state
      board[r][c] = temp
      return found

    for r in range(ROWS):
      for c in range(COLS):
        if board[r][c] == word[0]:
          if dfs(r, c, 0):
            return True

    return False