class Solution:
    def lenLongestSubStr(self, s):
        my_set = set()
        maxLen = 0
        left = 0

        for right in range(len(s)):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
    
s = "bbbb"
s2 = "abcabcbb"
s3 = "pwwkew"

solution = Solution()

print(solution.lenLongestSubStr(s2))