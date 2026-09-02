from collections import deque

class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        
        # 1. Locate S, L items, and assign indices to L items
        litter_map = {}
        start_pos = None
        litter_count = 0
        
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_pos = (r, c)
                elif cell == 'L':
                    litter_map[(r, c)] = litter_count
                    litter_count += 1
        
        # Target mask when all litter is collected
        target_mask = (1 << litter_count) - 1
        
        # Initial mask check if 'S' happens to be on an 'L' (though problem states 'S' is separate)
        start_mask = 0
        if start_pos in litter_map:
            start_mask |= (1 << litter_map[start_pos])
            
        if start_mask == target_mask:
            return 0

        # Queue stores: (steps, r, c, current_energy, mask)
        queue = deque([(0, start_pos[0], start_pos[1], energy, start_mask)])
        
        # visited[r][c][mask] stores the maximum remaining energy seen for this state
        visited = {}
        visited[(start_pos[0], start_pos[1], start_mask)] = energy
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            steps, r, c, cur_e, mask = queue.popleft()
            
            # Prune if we found a strictly better path to this exact state with more energy
            if visited.get((r, c, mask), -1) > cur_e:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries and obstacles
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_e = cur_e - 1
                    
                    if next_e < 0:
                        continue  # Not enough energy to make the step
                    
                    cell_type = classroom[nr][nc]
                    
                    # Handle Reset 'R'
                    if cell_type == 'R':
                        next_e = energy
                    
                    # Handle Litter 'L'
                    next_mask = mask
                    if (nr, nc) in litter_map:
                        next_mask |= (1 << litter_map[(nr, nc)])
                    
                    # Check if all litter collected
                    if next_mask == target_mask:
                        return steps + 1
                    
                    # If energy reaches 0 and cell is NOT 'R', student cannot move from here, skip pushing to queue
                    if next_e == 0 and cell_type != 'R':
                        continue
                    
                    # State relaxation: only visit if we reach this (nr, nc, next_mask) with strictly higher energy
                    if next_e > visited.get((nr, nc, next_mask), -1):
                        visited[(nr, nc, next_mask)] = next_e
                        queue.append((steps + 1, nr, nc, next_e, next_mask))
                        
        return -1