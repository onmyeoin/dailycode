from collections import Counter
import re

class Solution:
    def most_common_word(self, paragraph, banned):
        clean_words = re.findall(r'\w+', paragraph.lower())
        not_banned = [word for word in clean_words if word not in banned]
        most_common = Counter(not_banned)
        return(most_common.most_common(1)[0][0])


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

solution = Solution()

print(solution.most_common_word(paragraph,banned))