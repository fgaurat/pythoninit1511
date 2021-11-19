#import fibo
#import fibo as f
import sys
from fibo import fib2 as f2

def fib2():
    print("toto")

def main(value):
    f = f2(value)
    fib2()
    print(f)
    print("name", __name__)

if __name__ == "__main__":
    print(sys.argv)
    value = int(sys.argv[1])
    main(value)