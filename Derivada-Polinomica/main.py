#guarda los numeros base de los polinomios
def pedirDatosPolinomicos(grado):
  lista = []
  
  for x in range(0, grado + 1, 1):
    
    print("Ingrese el polinomia de grado",grado - x, end ="")
    grabar = int(input(": "))
    lista.append(grabar)
  
  return lista

#deriva los numeros base
def derivarPolinomio(datosDerivar):
  
  derivado = datosDerivar.copy()
  print("original: ",datosDerivar)
  print("duplicado: ",derivado)
  
  return derivado

#muestra el polinomio original
def ordenarPolinomio():
  
  copia = listaDatos.copy()
  ex = "x"
  elevar = "^"
  mas = "+"
  palabra = "{}{}{}{}"
  
  for x in range(0, len(copia ) - 1, 1):
    print(palabra.format(copia[x], ex, elevar, len(copia) - x - 1), end = "")
    if copia[x+1] > 0:
      print(mas, end = "")
  print(copia[gradoPolinomica], end = "")
    
#obtener datos
gradoPolinomica = int(input("Ingrese el grado del polinomio: "))
listaDatos = pedirDatosPolinomicos(gradoPolinomica)
print(listaDatos)

ordenarPolinomio()