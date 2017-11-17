def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b

for index, fibonacci_number in enumerate(fib()):
     print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))
     if index == 10:
         break
