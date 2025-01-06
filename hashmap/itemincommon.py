list1 = [1,2,5]
list2 = [3,4,5]

class Solution:
    def item_in_common(self, l1, l2):
        my_dict ={}
        for i in l1:
            my_dict[i] = True
        
        for j in l2:
            if j in my_dict:
                return True
        return False

solution = Solution()

print(solution.item_in_common(list1, list2))
