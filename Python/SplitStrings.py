""" 
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

"""

def solution(s):
    resp = []
    for x in range(len(s)):
        if ((x % 2) ==  0):
            if(len(s[x:x+2]) < 2):
                resp.append(s[x:x+2]+'_')
            else:
                resp.append(s[x:x+2])

    print(resp)
solution("Holas")