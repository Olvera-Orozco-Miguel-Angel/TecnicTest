lista= [2.3, 5, 67, 5, 778, -11, 1, 0, 2]
aux = 0
counter = 0

for i in lista:
    while counter < len(lista)-1:
        if lista[counter] > lista[counter+1]:
            aux = lista[counter]
            lista[counter] = lista[counter+1]
            lista[counter+1] = aux
        counter += 1
    counter = 0

print(f"La listsa ordenada sería {lista}")
