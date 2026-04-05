# Find does not repeat characters

# Input: "aabbcdd"
# Output: c


def repeatCharacters(word: str) -> str:
    if len(word) == 0:
        return "Invalid Input"
    else:
        count = {}
        for i in range(0, len(word), +1):
            if word[i] in count:
                count[word[i]] += 1
            else:
                count[word[i]] = 1
        # return count
        for ch in count:
            if count[ch] == 1:
                return ch


print(repeatCharacters("aabbcdd"))
