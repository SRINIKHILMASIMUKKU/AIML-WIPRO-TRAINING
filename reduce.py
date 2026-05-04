from functools import reduce
num = [1,2,34,4,8]
res = reduce(lambda a, b:a+b, num)
print(res)
