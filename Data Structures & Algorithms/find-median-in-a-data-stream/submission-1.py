class MedianFinder:

    def __init__(self):
        self.nums = []
        self.median = 0

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.nums.sort()
        self.findMedian()
        return

    def findMedian(self) -> float:
        nums = self.nums
        mid = len(nums)//2
        if len(nums) % 2 == 1:
            self.median = nums[mid]
        else:
            avg = (nums[mid-1] + nums[mid])/2
            self.median = avg
        return self.median