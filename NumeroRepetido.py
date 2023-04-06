#10 :50
cadena = "1,1,1,1,1,3,5,5,6,6,6,6,7,7,748486986"
cadena +=",";
almacenarNumero = ""  # esta variable va guardando la cadena
arrayNumeros = []  #aquí se almacenan los numeros que tiene el arreglo
auxValor = []  #aquí se guarda la cantidad de cada arreglo
auxNumero =0  # despues de castear en el else almacenarNúmero esta variable sirve para guardar ese valor resultante
index  = 0
acumulador = 0;

for index,caracter in enumerate(cadena):
    if not(caracter == ",")  :
        almacenarNumero += caracter
        #print("N "+almacenarNumero)
    else:
       auxNumero = int (almacenarNumero)
       #print("C ",auxNumero)
       almacenarNumero = ""
       if auxNumero in arrayNumeros:
            index = arrayNumeros.index(auxNumero )
            auxValor[index] = (auxValor[index])+1;
            almacenarNumero = ""


       else:
           arrayNumeros.append(auxNumero)
           auxValor.append(1)
           almacenarNumero = ""


print(arrayNumeros)
print(auxValor)

for i, item in enumerate(auxValor):
    if item > acumulador:
        index = i;
        acumulador  = item

print(f"El número {arrayNumeros[index] }, se repite más veces con:  { auxValor[index] }, ")






