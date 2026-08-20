class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                # If we can leave the opponent in a losing state, we win
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check further k
                k += 1
                
        return dp[n]