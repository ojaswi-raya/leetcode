# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode) -> list[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        idx = 1  # 0-indexed position of `curr`
        
        first_idx = -1
        last_idx = -1
        min_dist = float('inf')
        
        while curr.next:
            nxt = curr.next
            
            # Check for local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_idx == -1:
                    first_idx = idx
                else:
                    min_dist = min(min_dist, idx - last_idx)
                
                last_idx = idx
            
            prev = curr
            curr = nxt
            idx += 1
            
        if first_idx == -1 or first_idx == last_idx:
            return [-1, -1]
            
        return [min_dist, last_idx - first_idx]