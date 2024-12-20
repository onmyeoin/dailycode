def majorityElement(nums):
    nums.sort()
    n = len(nums)
    return nums[n//2]


nums = [3,2,3]
majorityElement(nums)