class Solution:
    def lenLongestSubStr(self, s):
        left = 0
        maxLen = 0
        my_set = set()

        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            maxLen = max(maxLen, right - left +1)
        return maxLen

s = "bbbb"
s2 = "abcabcbb"
s3 = "pwwkew3ka99"

solution = Solution()

print(solution.lenLongestSubStr(s3))