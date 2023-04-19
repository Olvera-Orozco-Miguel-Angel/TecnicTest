"""
Crea una función que tome como entrada una cadena de texto y devuelva el número de caracteres que hay en ella.
"""

cadena = "sono michelangelo"
counter = 0
work = True
while cadena[counter:]:
    counter = counter+1
    print("Entre ",counter)

try:
    while work:
        cadena[counter]
        counter = counter + 1;

except:
    print("El total es: ", counter)
    work = False