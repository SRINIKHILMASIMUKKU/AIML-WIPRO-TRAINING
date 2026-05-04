n = [(1,3), (2, 1), (4, 2)]
a = len(n)
for i in range(a):
    for j in range(i+1, a):
        if n[i][1] > n[j][1]:
            n[i], n[j] = n[j], n[i]
print(n)
