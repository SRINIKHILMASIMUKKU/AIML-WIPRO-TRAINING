a = list(map(int, input().split()))
n = len(a)+1
e = n*(n+1)//2
ac = sum(a)
print(e-ac)
