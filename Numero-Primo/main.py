import suma as s

#main
def main():
  #Pedimos el dato al usuario(cualquier número) e imprimimos
  num = int(input("Ingrese número: "))#lo convertimos a un dato "int"
  mostrar = numPrimo(num)#
  print(mostrar)

  valorSuma = s.suma(3, 25)
  print("Suma: ",valorSuma)

#función que recive un número cualquiera y calcula si es un número primo o no
def numPrimo(entrada):
    respuesta = ""
    contador = 0;
    
    for x in range(1, entrada + 1, 1):
        if entrada % x == 0:
            contador += 1
        
    if contador == 2:
        respuesta = "El número es primo"
    else:
        respuesta = "El número no es primo"
        
    return respuesta

if __name__ == '__main__':
  main()




