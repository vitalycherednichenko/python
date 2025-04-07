"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').
"""

def solution(string):
    result = []
    str_len = len(string)
    for i in range(0, str_len, 2):
        substr = string[i]
        if i + 1 == str_len:
            substr += '_'
        else:
            substr += string[i + 1]
        result.append(substr)
    return  result


print(solution("abcde"))
