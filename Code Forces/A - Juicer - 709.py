n, b, d = (int(x) for x in input().split())
a = ([int(x) for x in input().split()])
a_ = []

t = 0
for size in a:
    if size <= b:
        a_.append(size)
    if sum(a_) > d:
        t += 1
        a_ = []

print(t)

