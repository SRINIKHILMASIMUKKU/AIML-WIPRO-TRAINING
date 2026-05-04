def my_gen():
    yield 10
    yield 20
    yield 90
gen = my_gen()
for i in gen:
    print(i)
