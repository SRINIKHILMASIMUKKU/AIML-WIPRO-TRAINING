from multiprocessing import Pool
def square(n):
    return n*n
if __name__ == "__main__":
    num = [1, 2, 3, 4]
    with Pool(2) as p:
        res = p.map(square, num)
    print(res)
