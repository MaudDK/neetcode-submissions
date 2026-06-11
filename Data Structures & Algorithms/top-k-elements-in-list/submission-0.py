class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        buckets = [[] for i in range(len(nums)+1)]

        for num in nums:
            counts[num]+=1
        
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for val in buckets[i]:
                result.append(val)
                if len(result) == k:
                    return result
    
        