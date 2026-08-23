class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Compare characters position by position
        for i in range(len(strs[0])):
            char = strs[0][i]
            
            for s in strs[1:]:
                # If index exceeds string length or characters mismatch
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
                    
        return strs[0]