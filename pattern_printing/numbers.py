#1
#12
#123
#1234
#12345

def number_pattern(num):
    if num == 0:
        print("Invalid Input")
    else:
        for i in range(1, num+1,+1):
            for j in range(1, i+1):
                print("*", end =" ")
            print()
number_pattern(5)