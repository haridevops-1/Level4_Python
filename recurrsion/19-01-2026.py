nums= [0,1,1,2,3,4,5,6,7]

def fibonacci_series(input, arr):
    if len(arr) == 0 or input == 0:
        return "Invalid Input"
    else:
        for i in range(0,len(arr),+1):
            if input == i: