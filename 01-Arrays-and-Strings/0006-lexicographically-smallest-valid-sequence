class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # last[j] = index in word1 used to match
        # word2[j:] as far to the right as possible.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = [0] * m

        # Whether we have already used our one mismatch.
        can_skip = True

        j = 0

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans[j] = i
                j += 1

            # Use this position as the one mismatch
            elif can_skip and (
                j == m - 1 or i < last[j + 1]
            ):
                ans[j] = i
                j += 1
                can_skip = False

        if j != m:
            return []

        return ans