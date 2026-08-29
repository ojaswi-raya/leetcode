class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        # Pair values with original indices and sort by value
        sorted_pairs = sorted((val, i) for i, val in enumerate(nums))
        
        res = [0] * n
        
        # Group adjacent elements whose difference <= limit
        group_vals = []
        group_indices = []
        
        for val, idx in sorted_pairs:
            # If starting a new group because limit is exceeded
            if group_vals and val - group_vals[-1] > limit:
                # Assign sorted values to sorted indices for the completed group
                group_indices.sort()
                for i in range(len(group_vals)):
                    res[group_indices[i]] = group_vals[i]
                
                # Reset for the new group
                group_vals = []
                group_indices = []
            
            group_vals.append(val)
            group_indices.append(idx)
        
        # Process the final remaining group
        if group_vals:
            group_indices.sort()
            for i in range(len(group_vals)):
                res[group_indices[i]] = group_vals[i]
                
        return res