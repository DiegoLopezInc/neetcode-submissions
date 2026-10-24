class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            looking = target - n
            if looking in seen:
                return [seen[looking], i]
            seen[n] = i
            
            
        
        