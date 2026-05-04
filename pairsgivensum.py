a = list(map(int, input().split()))
target = int(input())
seen = set()
for num in a:
    if (target-num) in seen:
        print(target-num, num)
    seen.add(num)
