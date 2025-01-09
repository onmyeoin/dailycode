
from collections import Counter

def commonChars(words):
    common_count = Counter(words[0])
    
    # Iterate over the remaining words
    for word in words[1:]:
        # Update the counter to keep only the minimum count of common characters
        common_count &= Counter(word)
    
    # Expand the characters back to a list
    result = []
    for char, count in common_count.items():
        result.extend([char] * count)
    
    return result

# Example 1
words1 = ["bella", "label", "roller"]
print(commonChars(words1))  # Output: ["e", "l", "l"]

# Example 2
words2 = ["cool", "lock", "cook"]
print(commonChars(words2))  # Output: ["c", "o"]