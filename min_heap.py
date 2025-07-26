import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def remove_min(self):
        if not self.heap:
            return None
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0
