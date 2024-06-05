def main():
  alumno1 = Alumno()
  alumno2 = Alumno()
  
  alumno1.datos("armando",4)
  alumno2.datos("jackeline",9)
  
  alumno1.imprimir()
  alumno1.condicion()
  print("------------------------------")
  alumno2.imprimir()
  alumno2.condicion()
  

class Alumno:
  def datos(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

  def imprimir(self):
    print("Nombre: ", self.nombre)
    print("Nota: ",self.nota)

  def condicion(self):
    if self.nota < 5:
      print("El alumno ha reprobado")
    else:
      print("El alumno ha parobado")

if __name__ == '__main__':
  main()