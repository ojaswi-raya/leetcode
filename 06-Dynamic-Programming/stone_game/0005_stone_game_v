class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        
        # Build prefix sums
        prefix = stones[:]
        for i in range(1, n):
            prefix[i] += prefix[i - 1]
            
        # Base case: if forcing pick at last index n - 1
        ans = prefix[-1]
        
        # Backward iteration from n - 2 down to 1
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefix[i] - ans)
            
        return ans