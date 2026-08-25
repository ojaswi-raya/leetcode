class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        has_non_zero = False
        
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_non_zero = True
                
        # If all elements are 0, no non-zero XOR subsequence can be formed
        if not has_non_zero:
            return 0
            
        # If total XOR is already non-zero, take the whole array
        if total_xor != 0:
            return len(nums)
            
        # Otherwise, removing 1 non-zero element makes the XOR non-zero
        return len(nums) - 1