class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        ordered = sorted(seen, key=lambda count: seen[count], reverse=True)

        return ordered[:k]