class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            self.resolveBattle(maxHeap)
        
        maxHeap.append(0)
        return -maxHeap[0]
            
    
    def resolveBattle(self, maxHeap):
        k1 = heapq.heappop(maxHeap)
        k2 = heapq.heappop(maxHeap)

        if k1 != k2:
            new = k1 - k2
            heapq.heappush(maxHeap, new)

        