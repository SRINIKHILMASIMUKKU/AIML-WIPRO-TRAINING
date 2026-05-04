p = list(map(int, input().split()))
d = {}
for i in p:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
