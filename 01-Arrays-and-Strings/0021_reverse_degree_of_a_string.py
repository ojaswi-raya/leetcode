class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        
        for idx, char in enumerate(s, start=1):
            # Calculate reversed alphabet value ('a' -> 26, 'z' -> 1)
            reversed_val = 26 - (ord(char) - ord('a'))
            
            # Multiply value by 1-based string index and add to sum
            total_sum += reversed_val * idx
            
        return total_sum