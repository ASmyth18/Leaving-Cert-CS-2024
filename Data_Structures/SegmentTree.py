"""
Implement a segment tree data structure that supports range sum queries and updates.
The segment tree should be able to efficiently find the sum of elements in a given range and update individual elements.
"""

class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, index, left, right):
        if left == right:
            self.tree[index] = nums[left]
            return

        mid = (left + right) // 2
        self._build(nums, 2 * index + 1, left, mid)
        self._build(nums, 2 * index + 2, mid + 1, right)
        self.tree[index] = self.tree[2 * index + 1] + self.tree[2 * index + 2]

    def update(self, index, val):
        self._update(index, val, 0, 0, self.n - 1)

    def _update(self, index, val, node, left, right):
        if left == right:
            self.tree[node] = val
            return

        mid = (left + right) // 2
        if index <= mid:
            self._update(index, val, 2 * node + 1, left, mid)
        else:
            self._update(index, val, 2 * node + 2, mid + 1, right)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, left, right):
        return self._query(left, right, 0, 0, self.n - 1)

    def _query(self, left, right, node, node_left, node_right):
        if left > node_right or right < node_left:
            return 0

        if left <= node_left and node_right <= right:
            return self.tree[node]

        mid = (node_left + node_right) // 2
        left_sum = self._query(left, right, 2 * node + 1, node_left, mid)
        right_sum = self._query(left, right, 2 * node + 2, mid + 1, node_right)
        return left_sum + right_sum
    
# Initialize the segment tree with an array of numbers
nums = [1, 3, 5, 7, 9, 11]
segment_tree = SegmentTree(nums)

# Perform range sum queries
print(segment_tree.query(0, 2))  # Output: 9 (sum of elements from index 0 to 2)
print(segment_tree.query(1, 4))  # Output: 24 (sum of elements from index 1 to 4)
print(segment_tree.query(2, 5))  # Output: 32 (sum of elements from index 2 to 5)

segment_tree.update(2, 10)  # Update the element at index 2 to 10

# Perform range sum queries after the update
print(segment_tree.query(0, 2))  # Output: 14 (sum of elements from index 0 to 2)
print(segment_tree.query(1, 4))  # Output: 29 (sum of elements from index 1 to 4)
print(segment_tree.query(2, 5))  # Output: 37 (sum of elements from index 2 to 5)