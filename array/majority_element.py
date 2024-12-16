class Solution:
    def majorityElement(self, nums):    
        nums = [2,2,1,1,1,2,2]
        nums.sort()
        n = len(nums)
        nums[n//2]