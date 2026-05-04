def my_deco(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
@my_deco
def say_hello():
    print("Hello")
say_hello()
