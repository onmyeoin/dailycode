class Solution:
    def lengthOfLongestSubstring(self, s):
        maxLen = 0
        left = 0
        my_set = set()

        for right in range(len(s)):
            # if char is already in set, remove it from left
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            # Add the current char to the set
            my_set.add(s[right])
            #update max len
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen

s = "bbbb"
s2 = "abcabcbb"
s3 = "pwwkew"

solution = Solution()

print(solution.lengthOfLongestSubstring(s2))