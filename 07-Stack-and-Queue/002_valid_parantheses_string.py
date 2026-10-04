class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open = 0
        max_open = 0
        
        for char in s:
            if char == '(':
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            else:  # char == '*'
                min_open -= 1  # Treat '*' as ')'
                max_open += 1  # Treat '*' as '('
            
            # Too many ')' - impossible to form a valid string
            if max_open < 0:
                return False
            
            # min_open cannot be negative (can't have negative active '(')
            if min_open < 0:
                min_open = 0
                
        # Valid if 0 active open parentheses is within our valid range
        return min_open == 0