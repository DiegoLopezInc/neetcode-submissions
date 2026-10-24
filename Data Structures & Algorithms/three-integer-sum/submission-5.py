class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # check 
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            # two pointer
            l, r = i+1, len(nums) - 1
            while l < r:
                sum_ = a + nums[l] + nums[r]
                if sum_ == 0:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while l < r and l > 1 and nums[l] == nums[l-1]:
                        l+=1
                elif sum_ < 0:
                    l+=1
                else: r-=1

        return res
                
