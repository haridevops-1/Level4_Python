# Check if Palindrome or not

# Example:
## Input: "madam"
## Output: Palindrome


def to_CheckPalindrome_orNot(words: str):
    if len(words) == 0:
        return "Invalid Input"
    else:
        rev_word = ""
        for i in range(len(words) - 1, -1, -1):
            rev_word = rev_word + words[i]
        # print(rev_word)
        if rev_word == words:
            return "Palindrome"
        return "Not a Palindrome"


print(to_CheckPalindrome_orNot("madam"))

print(to_CheckPalindrome_orNot("teacher"))
