class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        left_sum = sum(int(c) for c in num[:half] if c != '?')
        right_sum = sum(int(c) for c in num[half:] if c != '?')
        
        left_q = num[:half].count('?')
        right_q = num[half:].count('?')
        
        delta_sum = left_sum - right_sum
        delta_q = left_q - right_q
        
        # If net '?' count is odd, Alice always wins
        if delta_q % 2 != 0:
            return True
        
        # Bob wins (return False) iff the net '?' can offset the net sum using 9 per pair
        return delta_sum + (delta_q // 2) * 9 != 0