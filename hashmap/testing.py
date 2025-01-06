class Solution:
    def majority_element(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]
    
nums = [3,2,3]

solution = Solution()

print(solution.majority_element(nums))