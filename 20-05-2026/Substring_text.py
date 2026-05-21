# Question 2:

# Given two strings txt and pat, the task is to find if pat is a substring of txt. If yes, return the index of the first occurrence, else return -1.
# NO IN-BUILT FUNCTIONS ALLOWED. @channel


# Input: txt = "hello world", pat = "world", output = 6
# Input: txt = "programming", pat = "gram"  output = 3
# Input: txt = "abcdef", pat = "xyz" output = -1 (no pattern matches)
# Input: txt = "aaaaaa", pat = "aab"  output = 0


def is_Substring_text(txt: str, pat: str):
    # if len(txt) or len(pat) == 0:
    #     return "Invalid Input"
    result = ""
    for i in range(0, len(txt), +1):
        if pat[0] == txt[i]:
            result = result + str(i)
            break
    if len(result) == 0:
        return -1
    return result


print(is_Substring_text("hello world", "world"))
print(is_Substring_text("programming", "gram"))
print(is_Substring_text("abcdef", "xyz"))
print(is_Substring_text("aaaaaa", "aa"))
