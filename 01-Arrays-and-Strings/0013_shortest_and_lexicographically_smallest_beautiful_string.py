class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Collect indices of all '1's in the string
        ones = [i for i, ch in enumerate(s) if ch == '1']
        
        # If there are fewer than k '1's, no beautiful substring exists
        if len(ones) < k:
            return ""
        
        min_len = float('inf')
        ans = ""
        
        # Slide a window of size k over the indices of '1's
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            candidate = s[start : end + 1]
            length = len(candidate)
            
            # Check if candidate is shorter, or same length but lexicographically smaller
            if length < min_len:
                min_len = length
                ans = candidate
            elif length == min_len:
                if candidate < ans:
                    ans = candidate
                    
        return ans