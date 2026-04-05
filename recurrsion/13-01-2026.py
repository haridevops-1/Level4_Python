## factorial of n


# n= 5

def factorial(n):
    if n == 0:
        return "invalid input"
    elif n==1:
        return 1
    while n >1:
        return n* factorial(n-1)
    
print(factorial(5))
print(factorial(6))
print(factorial(7))

