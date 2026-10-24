class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        # t = 10
        # nums = [4,5,6]
        for i, n in enumerate(nums):
            comp = target - n
            if comp in seen: 
                    return [seen[comp], i]
            seen[n] = i