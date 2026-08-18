class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        # Case 1: k equals array length -> entire array is the only subarray
        if k == n:
            return max(nums)
        
        # Case 2: k == 1 -> find max element that appears exactly once in nums
        if k == 1:
            ans = -1
            for x in set(nums):
                if nums.count(x) == 1:
                    ans = max(ans, x)
            return ans
        
        # Case 3: 1 < k < n -> only boundary elements can appear in exactly 1 subarray
        candidates = []
        
        # Check first element
        if nums.count(nums[0]) == 1:
            candidates.append(nums[0])
            
        # Check last element
        if nums.count(nums[-1]) == 1:
            candidates.append(nums[-1])
            
        return max(candidates) if candidates else -1