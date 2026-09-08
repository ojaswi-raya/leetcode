class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        dp = 0  # Total distinct non-empty subsequences so far
        last = {}  # Tracks the contribution added by each character

        for char in s:
            # New distinct subsequences introduced by appending 'char'
            added = (dp + 1 - last.get(char, 0)) % MOD
            
            # Update total count
            dp = (dp + added) % MOD
            
            # Record total contribution for this character
            last[char] = (last.get(char, 0) + added) % MOD

        return dp