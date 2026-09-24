class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            # Sum the digits of the integer
            digit_sum = sum(int(digit) for digit in str(val))
            
            if digit_sum == i:
                return i
                
        return -1