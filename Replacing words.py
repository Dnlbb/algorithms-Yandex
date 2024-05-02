dictionary = input().split()
text = input().split()
dictionary_set = set(dictionary)
result = []
for word in text:
    shword = word
    possible_shortenings = [word[:i] for i in range(1, len(word) + 1) if word[:i] in dictionary_set]
    if possible_shortenings:
        shword = min(possible_shortenings, key=len)
    result.append(shword)
print(' '.join(result))
