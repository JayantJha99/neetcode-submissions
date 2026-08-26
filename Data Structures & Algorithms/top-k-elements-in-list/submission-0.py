class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        res = []

        for num, count in freq.items():
            heapq.heappush(heap, [-count, num])

        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res