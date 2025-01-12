from collections import Counter
import re

class Solution:
   def most_common_word(self, paragraph, banned):
    words = re.findall(r'\w+', paragraph.lower())
    
    banned_set = set(banned)
    filtered_words = [word for word in words if word not in banned_set]

    word_count = Counter(filtered_words)
    
    most_common = word_count.most_common(1)[0][0]  # Get the word with the highest frequency
    
    return most_common


      



        





