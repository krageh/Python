# heights = [1, 1, 4, 2, 1, 3]
heights = [1, 2, 3, 4, 5]
heights_sorted = sorted(heights)
c = 0
for i in range(len(heights)):
    if heights[i] != heights_sorted[i]:
        c += 1
print(c)

