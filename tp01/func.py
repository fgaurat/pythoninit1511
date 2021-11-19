
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n=10):    # write Fibonacci series up to n
    """Return a Fibonacci series up to n."""
    a, b = 0, 1
    l = []
    while a < n:
        l.append(a)
        a, b = b, a+b
    return l
fib(10)
a = fib2(50)
b = fib2()
print(a)# [0,1,1,2,3,5,8]
print(b)
print(50*'-')


c = fib2(n=50)
print(c)

def add(a=0,b=0):
    return a+b

c = add(b=1)
c = add(b=2)
print(type(c))