# Count the number of vowels between the given consonants
# Given a string S, count how many vowels {a,e,i,o,u} occur between the two consonants.
# Assume that the consonants are given in pairs inside a list and those two consonants always exist inside the given string S.
# Sample test case 1:
# Input : S=“abcideouf”, C=[‘d’,’f’]
# Output: 3 #Explanation: in between ‘d’ and ‘f’ there are three vowels -> ‘e’ , ‘o’ , ‘u’

# Sample test case 2:
# Input : S="aeibcfou", C=['b', 'c']
# output: 0 #Explanation: no vowels exists between b and c

def FindVowels(S, C):
    if len(S)  == 0:
        return "Invalid Input"
    else:
        start = 0
        end = 0
        for i in range(0,len(S),+1):
            if C[0] == S[i]:
                start = i
            elif C[1] == S[i]:
                end = i
        print(start, end)
print(FindVowels("aeibcfou", C=['d','f']))