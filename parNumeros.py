"""
4.	Dado un arreglo de números enteros, escribe una función que determine si existe un par de elementos en el arreglo
 cuya suma sea igual a un número dado. Por ejemplo, si el arreglo es [1, 2, 3, 4, 5] y el número es 7,
 el resultado debería ser True ya que 2 + 5 = 7.

"""

"""  lo que yo propongo es crear una busqueda los números de moto que solo quede uno. y despues un for para que
solo se buquen los número que ya estan en el arreglo.
"""
auxuu = [0,1,2,3,4,5,6,7,8,9,10,11,12]
array = [2,5,4,6,7,8,3,2,1,2, 3, 4, 5]

number = 4
count = 0
j = 0
""" 
for i in array:
    if not i in auxArray:
        auxArray.append(i)
 """
print(len(array))
count = 0
for indice , i in enumerate(array):
    if i < number:
        while j < len(array)-1:
            #print(f"{i}  + {array[j+1]} = {i + array[j+1]}    | count {count}")
            #print(f"{array[indice]} + {array[j + 1]} ")
            if (array[count] + array[j+1]) == number:
                print(f"True {i} + {array[j + 1]} = {number}    ! {i} , {j+1}")

            j +=1
    count = count+1
    j =  count
    count =count-1
    print(f"j vale {j} y el indice vale {indice}")





