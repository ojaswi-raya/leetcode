from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        best_i = -1
        best_char = ''
        
        # Identify the rightmost position `i` where we can pick a character > target[i]
        for i in range(n):
            char_t = target[i]
            
            # Look for a character larger than target[i]
            for c in sorted(total_counts.keys()):
                if c > char_t and total_counts[c] > 0:
                    best_i = i
                    best_char = c
            
            # Extend prefix match if target[i] is available
            if total_counts[char_t] > 0:
                total_counts[char_t] -= 1
            else:
                break
        
        if best_i == -1:
            return ""
        
        # Reconstruct the string
        counts = Counter(s)
        res = []
        
        # 1. Matching prefix [0 ... best_i - 1]
        for i in range(best_i):
            res.append(target[i])
            counts[target[i]] -= 1
            
        # 2. Place smallest character larger than target[best_i]
        res.append(best_char)
        counts[best_char] -= 1
        
        # 3. Fill suffix with remaining available characters in sorted order
        for c in sorted(counts.keys()):
            res.append(c * counts[c])
            
        return "".join(res)