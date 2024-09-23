
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

''' 0 1 1 2 3 5 8 13 21... '''

def febSeq(n):
    for i in range(0,n):
        print(fibonacci(i), end=' ')

febSeq(10)