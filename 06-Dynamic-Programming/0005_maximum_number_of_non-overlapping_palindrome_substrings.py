class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0
        
        while i < n:
            # Check if a palindrome of length k or k + 1 starts at index i
            # Case 1: Palindrome of length k ending at i + k - 1
            if i + k <= n and s[i:i + k] == s[i:i + k][::-1]:
                ans += 1
                i += k  # Jump past this palindrome greedily
            # Case 2: Palindrome of length k + 1 ending at i + k
            elif i + k + 1 <= n and s[i:i + k + 1] == s[i:i + k + 1][::-1]:
                ans += 1
                i += k + 1  # Jump past this palindrome greedily
            else:
                i += 1
                
        return ans