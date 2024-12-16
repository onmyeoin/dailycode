class Solution:
    def remove_duplicates(self, nums):
        k = 0
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[k] = nums[i]
                k += 1
        
        return k