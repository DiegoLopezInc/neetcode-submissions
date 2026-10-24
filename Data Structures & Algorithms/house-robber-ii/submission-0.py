class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[:-1]), self.helper(nums[1:]))
         
        
    def helper(self, nums):
        rob_1, rob_2 = 0,0

        for n in nums:
            newRob = max(rob_1 + n, rob_2)
            rob_1 = rob_2
            rob_2 = newRob
        return rob_2
    