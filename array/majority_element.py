class Solution:
    def majorityElement(self, nums):    
        nums.sort()
        n = len(nums)
        nums[n//2]