def ProductOfDigits(n: int):
    if n <= 0:
        return "Invalid Input"
    else:
        answer = 1
        while n >=1:
            r = n % 10
            answer = answer * r
        return answer
    
print(ProductOfDigits(123))
    