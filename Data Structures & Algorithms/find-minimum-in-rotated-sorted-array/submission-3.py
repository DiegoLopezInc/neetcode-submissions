class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        min_ = nums[0]
        m = l+r//2
        while l <= r:
            if nums[l] < nums[r]:
                min_ = min(nums[l],min_)
                break

            m = (l+r)//2
            min_ = min(nums[m],min_)
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return min_

