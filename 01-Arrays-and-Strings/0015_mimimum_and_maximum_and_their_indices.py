class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        
        # Find indices of minimum and maximum elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Ensure i is the smaller index and j is the larger index
        i, j = min(min_idx, max_idx), max(min_idx, max_idx)
        
        # Calculate cost for each strategy
        both_from_front = j + 1
        both_from_back = n - i
        one_each_side = (i + 1) + (n - j)
        
        return min(both_from_front, both_from_back, one_each_side)