from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        
        # Preserve original indices: (l, r, weight, original_idx)
        sorted_intervals = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: x[0]
        )
        
        # Extract start times for fast binary search lookup
        starts = [x[0] for x in sorted_intervals]
        
        # Precompute next non-overlapping index for each interval
        next_indices = [bisect_right(starts, sorted_intervals[i][1]) for i in range(n)]
        
        # Memoization table for DP state: (i, count)
        # Store tuple: (score, tuple_of_original_indices)
        memo = {}

        def get_best(i: int, count: int):
            if i >= n or count == 0:
                return (0, ())
            
            state = (i, count)
            if state in memo:
                return memo[state]
            
            # Option 1: Skip interval i
            score_skip, idxs_skip = get_best(i + 1, count)
            
            # Option 2: Pick interval i
            l, r, w, orig_idx = sorted_intervals[i]
            nxt = next_indices[i]
            score_nxt, idxs_nxt = get_best(nxt, count - 1)
            
            score_pick = w + score_nxt
            # Maintain sorted order of original indices for correct comparison
            idxs_pick = tuple(sorted((orig_idx,) + idxs_nxt))
            
            # Choose best based on higher score, then lexicographically smaller indices
            if score_pick > score_skip:
                res = (score_pick, idxs_pick)
            elif score_skip > score_pick:
                res = (score_skip, idxs_skip)
            else:
                # Same score: prefer lexicographically smaller index list
                res = (score_pick, min(idxs_pick, idxs_skip))
            
            memo[state] = res
            return res

        _, result_indices = get_best(0, 4)
        return list(result_indices)