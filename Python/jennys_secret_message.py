"""
Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?

"""
def greet(name):
   if name == "Johnny":
        return "Hello, my love!"
   return "Hello, {name}!".format(name=name)

print(greet("James"))
print(greet("Jane"))
print(greet("Jim"))
print(greet("Johnny"))
## Best solution
# def calculate(s):
#     return str(eval(s.replace("plus", "+").replace("minus", "-")))

## Comentarios
# Es este caso es mejor utilizar el eval ya que nos permite evaluar el texto como codigo python
# Pero esto en otros contextos puede ser peligroso ya que no controla la entrada del texto
# Puede llegar a tener codigo malicioso.