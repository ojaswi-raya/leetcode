class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # Clamp circle's center coordinates to the bounds of the rectangle
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        
        # Calculate Euclidean distance squared from closest point to circle center
        dx = xCenter - closest_x
        dy = yCenter - closest_y
        
        # Overlap exists if distance^2 <= radius^2
        return (dx * dx + dy * dy) <= (radius * radius)