from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Group reserved seats by row (ignoring seats 1 and 10 as they don't affect 4-seat blocks)
        reserved_by_row = defaultdict(set)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved_by_row[row].add(seat)
        
        # Start assuming every row can accommodate 2 groups
        total_groups = n * 2
        
        # Adjust only for rows that have reserved seats
        for row, seats in reserved_by_row.items():
            left_free = not (seats & {2, 3, 4, 5})
            right_free = not (seats & {6, 7, 8, 9})
            middle_free = not (seats & {4, 5, 6, 7})
            
            if left_free and right_free:
                # Can fit 2 groups in this row (no reduction needed)
                continue
            elif left_free or right_free or middle_free:
                # Can fit 1 group in this row
                total_groups -= 1
            else:
                # Cannot fit any group in this row
                total_groups -= 2
                
        return total_groups