import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        def count_multiples(X: int) -> int:
            total_count = 0
            
            # Inclusion-Exclusion over all subsets
            for mask in range(1, 1 << n):
                current_lcm = 1
                bits_count = 0
                
                for i in range(n):
                    if mask & (1 << i):
                        bits_count += 1
                        current_lcm = math.lcm(current_lcm, coins[i])
                        if current_lcm > X:
                            break
                
                if current_lcm <= X:
                    multiples = X // current_lcm
                    if bits_count % 2 == 1:
                        total_count += multiples
                    else:
                        total_count -= multiples
                        
            return total_count

        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans