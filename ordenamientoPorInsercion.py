""" Aquí se muestra el algoritmo por inserción """
# 11:43 / 12:14

lista = [5,4,3,1,100,2,0,20,0,-1]
print( "Esta es la lista de arreglos a ordenar ",lista)
print(lista)

i = 1
j = 0
aux= 0

while i < len(lista):
      if lista[i-1] > lista[i]:
        aux =lista[i-1]
        lista[i-1] = lista[i]
        lista[i] = aux
        j = i-1
        while j > 0:
            if lista[j-1] > lista[j]:
                aux = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = aux
            else:
                break


            j= j-1

      i +=1
print(lista)