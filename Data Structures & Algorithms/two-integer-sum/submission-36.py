class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1, p2 = 0, 1
        i = 0
        for i in range(len(nums)):
            p2 = i + 1
            while p2 < len(nums):
                if nums[p1] + nums[p2] == target:
                    return [p1, p2] 
                p2 += 1
            p1 += 1
        
        return []
            
            
