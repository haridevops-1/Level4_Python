def MultiplyArray(num):
    if len(num) == 0:
        print("Invalid Input")
    else:
        result = []
        for i in range(0, len(num), +1):
            product = 1
            for j in range(0, len(num), +1):
                if i != j:
                    product = product * num[j]
            result.append(product)
        print(result, end="")


MultiplyArray([1, 2, 4, 8])
