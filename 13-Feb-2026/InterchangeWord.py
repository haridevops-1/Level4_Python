def is_InterchangeWord(sentence: str):
    if len(sentence) == 0:
        return "Invalid Input"
    else:
        words = sentence.split(" ")
        result = []
        indices = []
        for i in range(0, len(words), +1):
            if words[i] == "and":
                result.append(words[i])
                indices.append(i)
        l = len(words)
        for j in range(0, l, +1):
            idx = indices[j]
            temp = result[i - j - 1]
            sentence[idx] = idx
        return sentence


print(is_InterchangeWord("Jack and jill went up and down to get water"))
