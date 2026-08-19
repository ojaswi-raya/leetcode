class Solution:

  def generateParenthesis(self, n: int) -> list[str]:
    res = []

    def backtrack(current: str, open_count: int, close_count: int):
      if len(current) == 2 * n:
        res.append(current)
        return

      # Can add '(' if we haven't reached n open parentheses
      if open_count < n:
        backtrack(current + "(", open_count + 1, close_count)

      # Can add ')' only if it won't exceed the number of '(' placed
      if close_count < open_count:
        backtrack(current + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return res