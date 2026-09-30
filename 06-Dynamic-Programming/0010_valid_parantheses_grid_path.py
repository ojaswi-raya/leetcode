from functools import cache

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_len = m + n - 1
        
        # 1. Quick Pruning
        if total_len % 2 != 0:
            return False
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        max_open = total_len // 2

        @cache
        def dfs(r: int, c: int, open_count: int) -> bool:
            # Update running balance for current cell
            if grid[r][c] == '(':
                open_count += 1
            else:
                open_count -= 1

            # Invalid path state
            if open_count < 0 or open_count > max_open:
                return False

            # Destination reached: check if all parentheses balanced
            if r == m - 1 and c == n - 1:
                return open_count == 0

            # Move right or down
            ans = False
            if r + 1 < m:
                ans = ans or dfs(r + 1, c, open_count)
            if c + 1 < n:
                ans = ans or dfs(r, c + 1, open_count)

            return ans

        return dfs(0, 0, 0)