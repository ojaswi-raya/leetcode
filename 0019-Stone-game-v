from bisect import bisect_right


class Solution:

    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n == 1:
            return 0

        # Prefix sums for O(1) subarray sum queries
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]
        max_L = [[0] * n for _ in range(n)]
        max_R = [[0] * n for _ in range(n)]

        # Base case: single stone subproblems
        for i in range(n):
            max_L[i][i] = stoneValue[i]
            max_R[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = prefix[j + 1] - prefix[i]
                target = prefix[i] + total // 2

                # Find mid: largest k in [i, j-1] where prefix[k+1] - prefix[i] <= total // 2
                idx = bisect_right(prefix, target, i + 1, j + 1)
                mid = idx - 2  # k = idx - 2

                res = 0

                if mid >= i and (prefix[mid + 1] - prefix[i]) * 2 == total:
                    # Case 1: Equal split at k = mid
                    if mid - 1 >= i:
                        res = max(res, max_L[i][mid - 1])

                    res = max(
                        res,
                        prefix[mid + 1]
                        - prefix[i]
                        + max(dp[i][mid], dp[mid + 1][j]),
                    )

                    if mid + 2 <= j:
                        res = max(res, max_R[mid + 2][j])
                else:
                    # Case 2: Left < Right for k <= mid, Left > Right for k > mid
                    if mid >= i:
                        res = max(res, max_L[i][mid])

                    if mid + 2 <= j:
                        res = max(res, max_R[mid + 2][j])

                dp[i][j] = res
                val = total + res
                max_L[i][j] = max(max_L[i][j - 1], val)
                max_R[i][j] = max(max_R[i + 1][j], val)

        return dp[0][n - 1]