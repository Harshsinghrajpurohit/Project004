class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=n-1
        while l<h:
            m=(l+h)//2
            if nums[m]>nums[m+1]:
                h=m
            else:
                l=m+1
        return l
        