a = list(map(int, input().split()))
k = int(input())
j = a[-k:]+a[:-k]
print(j)
