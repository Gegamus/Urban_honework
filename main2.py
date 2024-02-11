def test(*args):
    print("test")
    print(args)
    for i, arg in enumerate(args):
        print(i,arg)


test(2, 'пример', 6)

def factorial(n):
    if n == 6:
        return 6
    factorial_n_plus_1 = factorial(n=n+1)
    return n + factorial_n_plus_1

print(factorial(1))