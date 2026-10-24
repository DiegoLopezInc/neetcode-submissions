class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        buffer = set(nums)
        if len(nums) > len(buffer):
            return True
        return False
            
        