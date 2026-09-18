class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Record first and last occurrence of each character
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
            
        valid_intervals = []
        
        # Step 2: Expand intervals for each character's starting position
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True
            
            curr = l
            while curr <= r:
                c = s[curr]
                # If a character inside starts before l, this l is invalid
                if first[c] < l:
                    valid = False
                    break
                # Expand right boundary to include all occurrences of character c
                r = max(r, last[c])
                curr += 1
                
            if valid:
                valid_intervals.append((l, r))
                
        # Step 3: Sort valid intervals by their end index (r)
        valid_intervals.sort(key=lambda x: x[1])
        
        ans = []
        prev_end = -1
        
        # Step 4: Greedy selection of non-overlapping intervals
        for l, r in valid_intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r
                
        return ans