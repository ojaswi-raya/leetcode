class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        prefix_map = {0: -1}  # prefix_sum -> index
        min_len = [float('inf')] * n  # min_len[i] = shortest length of valid subarray in arr[0..i]
        
        curr_sum = 0
        ans = float('inf')
        best_so_far = float('inf')
        
        for i, val in enumerate(arr):
            curr_sum += val
            prefix_map[curr_sum] = i
            
            # Check if there exists a subarray ending at i with sum == target
            needed = curr_sum - target
            if needed in prefix_map:
                left_idx = prefix_map[needed]
                curr_len = i - left_idx
                
                # Check if a non-overlapping valid subarray exists to the left
                if left_idx >= 0 and min_len[left_idx] != float('inf'):
                    ans = min(ans, curr_len + min_len[left_idx])
                
                best_so_far = min(best_so_far, curr_len)
            
            min_len[i] = best_so_far
            
        return ans if ans != float('inf') else -1