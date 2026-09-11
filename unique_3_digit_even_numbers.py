from collections import Counter

class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        count = Counter(digits)
        ans = 0
        
        # Iterate through all 3-digit even numbers
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            num_count = Counter([d1, d2, d3])
            
            # Check if all required digits are available
            if all(count[d] >= num_count[d] for d in num_count):
                ans += 1
                
        return ans