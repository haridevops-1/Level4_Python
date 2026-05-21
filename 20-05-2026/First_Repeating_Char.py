# Question 1:

# Given a string, find the first repeating character. For example, if the string is 'abcbca', the answer is 'a'. You can solve problem with dictionary and without dictionary.
# Test cases:


# Input: "abcbca", Output: "a"
# Input: "abcdef", Output: None
# Input: "aabbcc", Output: "a"
# Input :"", Output: None


def is_First_Repeating_Char(text: str):
    if len(text) == 0:
        return None
    else:
        empty_dict = {}
        for i in range(0, len(text), +1):
            if text[i] not in empty_dict:
                empty_dict[text[i]] = 1
            else:
                empty_dict[text[i]] += 1
        for char in empty_dict:
            if empty_dict[char] > 1:
                return char
        return None


print(is_First_Repeating_Char("abcbca"))
print(is_First_Repeating_Char("abcdef"))
print(is_First_Repeating_Char("aabbcc"))
print(is_First_Repeating_Char(""))
