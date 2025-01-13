from collections import Counter
import re

def most_common_word(paragraph, banned):
    clean_words = re.findall(r'\w+', paragraph.lower())
    not_banned = [word for word in clean_words if word not in banned]
    word_count = Counter(not_banned)
    print(word_count.most_common(1)[0][0])



paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

most_common_word(paragraph, banned)