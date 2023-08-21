

def DEBUG_print_rec(level):
    for i in range(level):
        print("\t", end="")

def fib(n, level):
    level += 1
    if(n == 1):
        DEBUG_print_rec(level)
        print('fib(1) = 1')
        return 1
    if(n == 2):
        DEBUG_print_rec(level)
        print('fib(2) = 1')
        return 1
    
    DEBUG_print_rec(level)
    print(f"fib({n-1}) + fib({n-2})")
    return fib(n-1, level) + fib(n-2, level)

level = 0
print(fib(15, level))

