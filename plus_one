from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the list in reverse (from right to left)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits  # No carry needed, return early
            
            digits[i] = 0  # 9 + 1 = 10, so set to 0 and continue loop to carry 1
            
        # If all digits were 9 (e.g., [9, 9] -> [0, 0]), we need an extra digit 1 at the front
        return [1] + digits