import suma as s
import resta as r
import multiplicacion as m
import division as d

def main():
  valorSuma = s.suma(25,10)
  print("Suma: ",valorSuma)

  valorResta = r.resta(15,5)
  print("Resta: ",valorResta)

  valorMultiplicacion = m.multiplicacion(5, 5)
  print("Multiplicación: ",valorMultiplicacion)

  valorDivision = d.division(10, 2)
  print("División: ",valorDivision)

if __name__ == '__main__':
  main()
  