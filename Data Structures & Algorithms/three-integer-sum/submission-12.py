class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):

            if i > 0 and nums[i-1] == nums[i]:
                continue

            l,r = i+1, len(nums)-1              
            while l < r:
                sum_ = n + nums[l] + nums[r]
                if sum_ > 0:
                    r-=1
                elif sum_ < 0:
                    l+=1
                else:
                    res.append([n, nums[l], nums[r]])
                    l+=1
                    while l < r and nums[l-1] == nums[l]:
                        l+=1
        return res


        