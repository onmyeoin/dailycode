import string
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]
clean_string = paragraph.translate(str.maketrans('','',string.punctuation))
clean1 = clean_string.split(',')
words = clean1.split()
clean_words = []


print(words)

for word in words:
    clean_words.append(word.lower())

counts = {}
for i in clean_words:
    counts[i] = counts.get(i, 0) + 1


for key in banned:
    if key in counts:
        counts.pop(key, None)

print(max(counts, key=counts.get))