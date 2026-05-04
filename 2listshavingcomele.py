l1 =  list(map(int, input().split()))
l2= list(map(int, input().split()))
c = list(set(l1) & set(l2))
if not c:
    print("NO")
else:
    print("YES")
