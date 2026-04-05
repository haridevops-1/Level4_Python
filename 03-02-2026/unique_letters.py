# Input = "apple"
# output ="It is not a unique"


def UniqueLetters(word: str):
    if len(word) == 0:
        print("Invalid Input")
    else:
        result = ""
        empty = ""
        for i in range(0, len(word), +1):
            if word[i] not in result:
                result += word[i]
            else:
                empty += word[i]
        if len(word) == len(result):
            print(word, "->", "It is having Unique Letters")
        else:
            print(word, "->", "It is not having unique Letters")


UniqueLetters("apple")
UniqueLetters("sky")
UniqueLetters("academy")
UniqueLetters("python")
UniqueLetters("White Board")


# Another method
def UniqueLettersAppear(word: str):
    if len(word) == 0:
        print("Invalid Input")
    else:
        count = 0
        for i in range(0,len(word),+1):
            for j in range(i+1, len(word),+1):
                if word[i] == word[j]:
                    count += 1
        if count > 0:
            return False
        return True
    
print(UniqueLettersAppear("apple"))
print(UniqueLettersAppear("sky"))
print(UniqueLettersAppear("academy"))
        