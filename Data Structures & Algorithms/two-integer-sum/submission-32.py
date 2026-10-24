class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            curr = target - n
            if curr in seen:
                return [seen[curr], i]
            seen[n]=i
        return []
