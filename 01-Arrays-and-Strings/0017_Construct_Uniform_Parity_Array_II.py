class Solution:

    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)

        # If min_val is odd, we can always make all elements odd.
        if min_val % 2 != 0:
            return True

        # If min_val is even, we can only succeed if ALL elements are even.
        for x in nums1:
            if x % 2 != 0:
                return False

        return True