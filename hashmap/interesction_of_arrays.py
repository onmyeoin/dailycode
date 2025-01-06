class Solution:
    def intersection(self, nums1, nums2):
        my_dict = {}
        my_set = set()

        for i in nums1:
            my_dict[i] = True
        
        for j in nums2:
            if j in my_dict:
                my_set.add(j)
        
        return list(my_set)
    
solution = Solution()

nums1 = [1,2,2,1]
nums2 = [2,2]

print(solution.intersection(nums1, nums2))