Solution Approach:
We need a Segment Tree or Fenwick Tree (BIT) to handle range maximum queries with point updates efficiently.

Update: O(log N)

Query: O(log N)

class Skyline:
    def __init__(self, buildings):
        self.n = len(buildings)
        self.tree = [0] * (4 * self.n)
        self.build(buildings, 1, 0, self.n - 1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
        else:
            mid = (l + r) // 2
            self.build(arr, node * 2, l, mid)
            self.build(arr, node * 2 + 1, mid + 1, r)
            self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, idx, val, node, l, r):
        if l == r:
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(idx, val, node * 2, l, mid)
            else:
                self.update(idx, val, node * 2 + 1, mid + 1, r)
            self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def query(self, ql, qr, node, l, r):
        if qr < l or ql > r:
            return float('-inf')
        if ql <= l and r <= qr:
            return self.tree[node]
        mid = (l + r) // 2
        left = self.query(ql, qr, node * 2, l, mid)
        right = self.query(ql, qr, node * 2 + 1, mid + 1, r)
        return max(left, right)
