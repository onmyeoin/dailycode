class Solution:
    def majorityElement(self, nums):
        from collections import Counter
        output=Counter(nums).most_common()[0][0]
        return output


