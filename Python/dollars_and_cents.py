"""
The company you work for has just been awarded a contract to build a payment gateway. In order to help move things along, you have volunteered to create a function that will take a float and return the amount formatting in dollars and cents.

39.99 becomes $39.99

The rest of your team will make sure that the argument is sanitized before being passed to your function although you will need to account for adding trailing zeros if they are missing (though you won't have to worry about a dangling period).

Examples:

3 needs to become $3.00

3.1 needs to become $3.10
Good luck! Your team knows they can count on you!

"""
def format_money(amount):
    amount_parts = str(amount).split(".")
    decimal = "00" if len(amount_parts) == 1 else amount_parts[-1]
    decimal = f"{decimal}0" if len(decimal) == 1 else decimal[:2] 
    return f"${amount_parts[0]}.{decimal}"

print(format_money(3))
print(format_money(3.1))

## Best solution
# def format_money(amount):
#     return '${:.2f}'.format(amount)

## Comentarios
# Usando el format con la instrucción : indicamos que es una instruccion de formato
# el .2f significa que seran dos cifras decimales y el f que es numero es un float