""" 
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
"""

def persistence(n):
    temp = n
    cont = 0
    while True:  
        digits = [int(y) for y in str(temp)]
        if(len(digits) > 1):
            aux = 1
            for i in digits:
                aux = aux * i
            temp = aux 
            cont = cont + 1
        else:
            break  

    return cont

print(persistence(4))