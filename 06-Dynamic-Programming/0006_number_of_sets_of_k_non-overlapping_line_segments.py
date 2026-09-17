import math

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # We need to compute combinations C(n + k - 1, 2 * k) % MOD
        total_points = n + k - 1
        choose = 2 * k
        
        return math.comb(total_points, choose) % MOD