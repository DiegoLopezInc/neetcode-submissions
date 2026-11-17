class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        order = sorted(count.items(), key=lambda item: item[1], reverse=True)

        return [num for num, _ in order[:k]]
       
            
