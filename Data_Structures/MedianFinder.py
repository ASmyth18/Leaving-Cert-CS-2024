"""
Design a data structure called "MedianFinder" that supports the following operations:
addNum(num) to add a number to the data structure and findMedian() to return the median of all numbers added so far.
The findMedian() operation should have an optimal time complexity.
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []  # smaller half of numbers
        self.min_heap = []  # larger half of numbers

    def addNum(self, num: int) -> None:
        # Add the new number to the max-heap
        heapq.heappush(self.max_heap, -num)

        # Balance the heaps if necessary
        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            max_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_num)

        # Ensure the size difference between heaps is at most 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            max_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_num)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            min_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_num)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
        
median_finder = MedianFinder()
median_finder.addNum(1)
median_finder.addNum(2)
print(median_finder.findMedian())  # Output: 1.5
median_finder.addNum(3)
print(median_finder.findMedian())  # Output: 2
median_finder.addNum(4)
print(median_finder.findMedian())  # Output: 2.5
median_finder.addNum(5)
print(median_finder.findMedian())  # Output: 3