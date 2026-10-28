#written 10.28.26
#generates numbers in the Fibonacci sequence
def fib_generator(n):
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1


g = fib_generator(10)
for i in range(10):
    print(next(g))


