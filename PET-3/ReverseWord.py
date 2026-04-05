# Given a string, the task is to reverse the order of the words in the given string. (Without using any inbuilt function)

# Examples:
# Input: s = “hello everyone”
# Output: s = “everyone hello”

# Input: s = “i love programming very much”
# Output: s = “much very programming love i”


def rev_sentence_by_word(sentence):
    # write your code
    not_space = ""
    result = []
    for i in range(0,len(sentence),+1):
        if sentence[i] != " ":
            not_space += sentence[i]
        if sentence[i] == " ":
            result.append(not_space)    
    return result

print(rev_sentence_by_word("i love programming very much"))
