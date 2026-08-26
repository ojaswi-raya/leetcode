class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            h = min(height[left], height[right])
            current_water = width * h
            
            # Track maximum volume
            max_water = max(max_water, current_water)
            
            # Shift the pointer pointing to the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water