def my_deco(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def say_hello():
    print("Hello")
decorated = my_deco(say_hello)
decorated()
