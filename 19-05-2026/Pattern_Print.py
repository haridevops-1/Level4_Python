'Write a python function print_pattern(n:int) '
'Given a number n=4, print the below pattern'

def is_PatternPrint(num: int):
    if num < 0:
        return 'Invalid Input'
    else:
        for i in range(1, num+1,+1):
            for j in range(1, i+1,+1):
                print(j, end = " ")
            print()

is_PatternPrint(4)