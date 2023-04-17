cadena="sono michelangelo"
aux = ""
index = len(cadena)-1

while index >= 0:
    aux += cadena[index]
    index -=1
print(f"The sentence is {cadena}\ninverted -> {aux}")




