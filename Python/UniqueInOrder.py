""" 
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.
"""

def unique_in_order(iterable):
    resp = []
    if len(iterable) > 0 :
        resp = [iterable[0]] 
        for it in iterable:
            if it != resp[-1]:
                resp.append(it)
    return resp

print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order(''))
