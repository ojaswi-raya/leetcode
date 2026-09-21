class Solution:
    def countSubarraysModuloK(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        
        # dp[r] stores the number of subarrays ending at the previous index with product % k == r
        dp = [0] * k
        
        for x in nums:
            val = x % k
            new_dp = [0] * k
            
            # 1. Extend existing subarrays ending at previous index
            for r in range(k):
                if dp[r] > 0:
                    new_dp[(r * val) % k] += dp[r]
            
            # 2. Start a new single-element subarray at current position
            new_dp[val] += 1
            
            # Add counts ending at current position to final result
            for r in range(k):
                result[r] += new_dp[r]
                
            dp = new_dp
            
        return result