from collections import Counter

class Solution:
    def largestOverlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        
        # Extract coordinates of all 1s in both images
        points1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        points2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Track counts of each translation vector (dr, dc)
        vector_counts = Counter()
        
        for r1, c1 in points1:
            for r2, c2 in points2:
                # Vector required to shift point from img1 to align with img2
                dr = r2 - r1
                dc = c2 - c1
                vector_counts[(dr, dc)] += 1
                
        # Return the maximum overlap count, or 0 if no 1s exist
        return max(vector_counts.values()) if vector_counts else 0