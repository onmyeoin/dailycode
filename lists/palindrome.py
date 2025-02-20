class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        start = 0
        end = len(strX)-1
        for _ in range(round(len(strX)/2)-1):
            if strX[start] == strX[end]:
                start += 1
                end -= 1
            else:
                return False
        return True 
    
solution = Solution()


x = 1231
solution.isPalindrome(x)

x = 1231
y = -121
z = 12321

len(str(x))
strX = str(x)
strX[2]
start = 0
end = len(strX)-1
# for i in range(len(strX)):
print(end)

range((len(strX)//2))

print(strX[start])
print(strX[end])  
start += 1
end -= 1
