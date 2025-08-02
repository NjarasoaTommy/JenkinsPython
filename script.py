def fibo(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("The parameter should be a positive number")
    else:
        return fibo(n - 1) + fibo(n - 2)
    
print(fibo(0))
print(fibo(1))
print(fibo(10))
