from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums, k):
        count = defaultdict(int)
        left = 0
        answer = 0

        for right in range(len(nums)):

            count[nums[right]] += 1

            while count[nums[right]] > k:
                count[nums[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer