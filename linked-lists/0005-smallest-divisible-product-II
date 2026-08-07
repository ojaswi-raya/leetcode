class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t
        t2 = t3 = t5 = t7 = 0
        temp = t
        for p, var in [(2, 2), (3, 3), (5, 5), (7, 7)]:
            cnt = 0
            while temp % p == 0:
                cnt += 1
                temp //= p
            if p == 2: t2 = cnt
            elif p == 3: t3 = cnt
            elif p == 5: t5 = cnt
            elif p == 7: t7 = cnt
            
        if temp > 1:
            return "-1"

        # Step 2: Precompute DP table for 2s and 3s
        MAX = 60
        dp = [[float('inf')] * (MAX + 1) for _ in range(MAX + 1)]
        dp[0][0] = 0
        for i in range(MAX + 1):
            for j in range(MAX + 1):
                if i == 0 and j == 0:
                    continue
                res = dp[i][j]
                res = min(res, 1 + dp[max(0, i - 1)][j])
                res = min(res, 1 + dp[i][max(0, j - 1)])
                res = min(res, 1 + dp[max(0, i - 2)][j])
                res = min(res, 1 + dp[max(0, i - 1)][max(0, j - 1)])
                res = min(res, 1 + dp[max(0, i - 3)][j])
                res = min(res, 1 + dp[i][max(0, j - 2)])
                dp[i][j] = res

        def min_digits(r2, r3, r5, r7):
            r2, r3 = max(0, r2), max(0, r3)
            r5, r7 = max(0, r5), max(0, r7)
            return r5 + r7 + dp[min(MAX, r2)][min(MAX, r3)]

        # Digit factor mappings
        f2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        f3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        f5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        f7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        N = len(num)
        z = N
        for k in range(N):
            if num[k] == '0':
                z = k
                break

        # Prefix factor sums
        p2, p3, p5, p7 = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
        for k in range(N):
            d = ord(num[k]) - ord('0')
            p2[k + 1] = p2[k] + f2[d]
            p3[k + 1] = p3[k] + f3[d]
            p5[k + 1] = p5[k] + f5[d]
            p7[k + 1] = p7[k] + f7[d]

        best_i, best_d = -1, -1

        # Search for longest matching prefix of length N
        for i in range(min(N, z), -1, -1):
            if i == N:
                if t2 <= p2[N] and t3 <= p3[N] and t5 <= p5[N] and t7 <= p7[N]:
                    return num
                continue

            r2 = max(0, t2 - p2[i])
            r3 = max(0, t3 - p3[i])
            r5 = max(0, t5 - p5[i])
            r7 = max(0, t7 - p7[i])

            start_d = ord(num[i]) - ord('0') + 1
            for d in range(start_d, 10):
                rem2 = max(0, r2 - f2[d])
                rem3 = max(0, r3 - f3[d])
                rem5 = max(0, r5 - f5[d])
                rem7 = max(0, r7 - f7[d])
                if min_digits(rem2, rem3, rem5, rem7) <= N - 1 - i:
                    best_i, best_d = i, d
                    break
            if best_i != -1:
                break

        # Case 1: Answer of same length N
        if best_i != -1:
            res = list(num[:best_i]) + [str(best_d)]
            r2 = max(0, t2 - p2[best_i] - f2[best_d])
            r3 = max(0, t3 - p3[best_i] - f3[best_d])
            r5 = max(0, t5 - p5[best_i] - f5[best_d])
            r7 = max(0, t7 - p7[best_i] - f7[best_d])

            for j in range(best_i + 1, N):
                for x in range(1, 10):
                    rem2 = max(0, r2 - f2[x])
                    rem3 = max(0, r3 - f3[x])
                    rem5 = max(0, r5 - f5[x])
                    rem7 = max(0, r7 - f7[x])
                    if min_digits(rem2, rem3, rem5, rem7) <= N - 1 - j:
                        res.append(str(x))
                        r2, r3, r5, r7 = rem2, rem3, rem5, rem7
                        break
            return "".join(res)

        # Case 2: Answer of length L > N
        else:
            M = min_digits(t2, t3, t5, t7)
            L = max(N + 1, M)
            res = []
            r2, r3, r5, r7 = t2, t3, t5, t7
            for k in range(L):
                for x in range(1, 10):
                    rem2 = max(0, r2 - f2[x])
                    rem3 = max(0, r3 - f3[x])
                    rem5 = max(0, r5 - f5[x])
                    rem7 = max(0, r7 - f7[x])
                    if min_digits(rem2, rem3, rem5, rem7) <= L - 1 - k:
                        res.append(str(x))
                        r2, r3, r5, r7 = rem2, rem3, rem5, rem7
                        break
            return "".join(res)