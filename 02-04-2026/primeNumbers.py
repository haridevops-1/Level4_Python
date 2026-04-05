def PrimeNumber(num: int):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, num):
        if num % i == 0:
            return False

    return True


print(PrimeNumber(21))  # False
print(PrimeNumber(40))  # False
print(PrimeNumber(3))  # True
print(PrimeNumber(9))  # False
