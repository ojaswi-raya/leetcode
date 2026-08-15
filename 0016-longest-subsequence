class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Step 1: Check if all elements are 0
        if all(x == 0 for x in nums):
            return 0
        
        # Step 2: Compute total XOR of all elements
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        # Step 3: If total_xor is already non-zero, we can use the whole array
        if total_xor != 0:
            return len(nums)
        
        # Step 4: If total_xor is 0, removing 1 non-zero element makes it non-zero
        return len(nums) - 1