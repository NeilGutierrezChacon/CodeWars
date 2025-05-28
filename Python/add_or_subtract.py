"""
In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

Note: the input will not be empty.

Examples
"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"

"""
def calculate(s: str):
   s = s.replace("minus", "|-").replace("plus", "|+").split("|")
   result = 0
   for s_part in s:
      result += int(s_part)
   return str(result)

print(calculate("1plus2plus3plus4"))
print(calculate("1plus2plus3minus4"))

## Best solution
# def calculate(s):
#     return str(eval(s.replace("plus", "+").replace("minus", "-")))

## Comentarios
# Es este caso es mejor utilizar el eval ya que nos permite evaluar el texto como codigo python
# Pero esto en otros contextos puede ser peligroso ya que no controla la entrada del texto
# Puede llegar a tener codigo malicioso.