def MaximumWords(sentence: list[str]):
    if len(sentence) == 0:
        return "Invalid Input"
    else:
        max_word = sentence[0]
        for i in range(0, len(sentence)):
            if sentence[i] > max_word:
                max_word = sentence[i]
        return max_word


print(MaximumWords(["apple", "academy", "students"]))
