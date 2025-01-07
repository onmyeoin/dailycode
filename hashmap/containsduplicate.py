class Solution:
    def containsduplicate(self, nums):
        my_dict = {}
        for num in nums:
            if num in my_dict:
                return True
            my_dict[num] = True
        return False

nums = [1,2,3,4]
#nums = [1,1,1,3,3,4,3,2,4,2]

solution = Solution()
print(solution.containsduplicate(nums))

"""
Most efficient


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set(nums)
        return len(nums) > len(unique_vals)



"""