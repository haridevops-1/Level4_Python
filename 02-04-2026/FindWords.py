## Hello This is very good place very nice
## very 2


def to_FindWords(sentence: str, word: str):
    if len(sentence) == 0:
        return "Invalid Input"
    else:
        result = ""
        count = 0
        Word = word
        Find = sentence.split()
        for i in range(0, len(Find), +1):
            # print(Find[i])
            if Find[i] == Word:
                count = count + 1
        result += str(count)
        return Word + " " + result


print(to_FindWords("Hello This is very good place very nice", "very"))
