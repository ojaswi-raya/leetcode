from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        
        # Determine the longest prefix of target that s can match
        pref_len = 0
        temp_counts = s_counts.copy()
        for i in range(n):
            if temp_counts[target[i]] > 0:
                temp_counts[target[i]] -= 1
                pref_len += 1
            else:
                break

        # Check positions from rightmost possible matching prefix down to 0
        for i in range(pref_len, -1, -1):
            if i == n:
                # Equal length match means s can form target exactly,
                # but we need strictly greater, so backtrack to i = n - 1
                continue
                
            # Compute remaining available characters after matching target[0...i-1]
            avail = s_counts.copy()
            for j in range(i):
                avail[target[j]] -= 1
            
            # Find the smallest character strictly greater than target[i]
            target_char = target[i]
            next_char = None
            for c in sorted(avail.keys()):
                if c > target_char and avail[c] > 0:
                    next_char = c
                    break
            
            if next_char:
                # Construct result: target[0...i-1] + next_char + sorted remaining chars
                res = list(target[:i])
                res.append(next_char)
                avail[next_char] -= 1
                
                for c in sorted(avail.keys()):
                    if avail[c] > 0:
                        res.append(c * avail[c])
                
                return "".join(res)
                
        return ""