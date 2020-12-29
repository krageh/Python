n, k = (int(x) for x in input().split())
import string
import random
word = []
word_ = word[:]

available = string.ascii_lowercase
while len(word) < n or len(word_) < k:
    x = random.choice(available)
    if len(word) > 1 and x == word[-1]:
        continue
    else:
        word.append(x)
        word_.append(x)
        if word.count(x) > 1:
            word_.remove(x)
        if len(word_) > k or (n - len(word)) < (k - len(word_)):
            word.pop()
        if len(word) < n and len(word_) == k:
            available = word_
            
# print(*word, sep='')
print(''.join(word))