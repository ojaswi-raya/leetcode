class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        ans = []
        depth = 0
        
        for char in seq:
            if char == '(':
                # Assign based on current depth parity, then increase depth
                ans.append(depth % 2)
                depth += 1
            else:
                # Decrease depth first, then assign based on new depth parity
                depth -= 1
                ans.append(depth % 2)
                
        return ans