class SegmentTree:
    def __init__(self, nums: list[int], k: int):
        self.n = len(nums)
        self.k = k
        self.tree_prod = [1] * (4 * self.n)
        self.tree_counts = [[0] * k for _ in range(4 * self.n)]
        self._build(nums, 1, 0, self.n - 1)

    def _merge(self, left_node: int, right_node: int, node: int):
        p1 = self.tree_prod[left_node]
        p2 = self.tree_prod[right_node]
        self.tree_prod[node] = (p1 * p2) % self.k

        counts = list(self.tree_counts[left_node])
        for r in range(self.k):
            new_r = (p1 * r) % self.k
            counts[new_r] += self.tree_counts[right_node][r]
            
        self.tree_counts[node] = counts

    def _build(self, nums: list[int], node: int, l: int, r: int):
        if l == r:
            val = nums[l] % self.k
            self.tree_prod[node] = val
            self.tree_counts[node] = [0] * self.k
            self.tree_counts[node][val] = 1
            return
        
        mid = (l + r) // 2
        self._build(nums, 2 * node, l, mid)
        self._build(nums, 2 * node + 1, mid + 1, r)
        self._merge(2 * node, 2 * node + 1, node)

    def update(self, node: int, l: int, r: int, idx: int, val: int):
        if l == r:
            mod_val = val % self.k
            self.tree_prod[node] = mod_val
            self.tree_counts[node] = [0] * self.k
            self.tree_counts[node][mod_val] = 1
            return

        mid = (l + r) // 2
        if idx <= mid:
            self.update(2 * node, l, mid, idx, val)
        else:
            self.update(2 * node + 1, mid + 1, r, idx, val)
            
        self._merge(2 * node, 2 * node + 1, node)

    def query(self, node: int, l: int, r: int, ql: int, qr: int) -> tuple[int, list[int]]:
        if ql <= l and r <= qr:
            return self.tree_prod[node], self.tree_counts[node]

        mid = (l + r) // 2
        if qr <= mid:
            return self.query(2 * node, l, mid, ql, qr)
        if ql > mid:
            return self.query(2 * node + 1, mid + 1, r, ql, qr)

        p1, c1 = self.query(2 * node, l, mid, ql, qr)
        p2, c2 = self.query(2 * node + 1, mid + 1, r, ql, qr)

        combined_prod = (p1 * p2) % self.k
        combined_counts = list(c1)
        for r_mod in range(self.k):
            new_r = (p1 * r_mod) % self.k
            combined_counts[new_r] += c2[r_mod]

        return combined_prod, combined_counts


class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = SegmentTree(nums, k)
        result = []

        for idx, val, start, x in queries:
            tree.update(1, 0, n - 1, idx, val)
            _, counts = tree.query(1, 0, n - 1, start, n - 1)
            result.append(counts[x])

        return result