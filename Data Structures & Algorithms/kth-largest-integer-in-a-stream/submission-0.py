class KthLargest:

    def __init__(self, k: int, sums: List[int]):
        self.minheap = sums
        self.k = k
        heapq.heapify(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
