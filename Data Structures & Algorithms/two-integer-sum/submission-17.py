class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, n in enumerate(nums):
            r = idx + 1
            while r < len(nums):
                total = nums[idx] + nums[r]
                if total == target:
                    return [idx,r]
                else:
                    r+=1
        return []