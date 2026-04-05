# Input = "Listen"
# Output = "silent"


def anagramString(left: str, right: str):
    count = 0
    result = ""
    for i in range(0, len(right), +1):
        if right[i] in left:
            count += 1
            result += right[i]
    if count == len(left) and len(result) == len(left):
        print(right, "It is Anagram")
    else:
        print(left, right, "It is not a anagram")


anagramString("listen", "silent")
anagramString('teacher','student' )