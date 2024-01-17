class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def presentarse(self):
        print(f"Hola! Me llamo {self.nombre} y tengo {self.edad} años")



class Trabajador(Persona):
    def __init__(self, nombre, edad, DNI, sueldo, cargo, empresa):
        super().__init__(nombre, edad, DNI)
        self.sueldo = sueldo
        self.cargo = cargo
        self.empresa = empresa
    
    def calcular_sueldo_anual (self):
        return 12 * self.sueldo
        

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, universidad, curso, asignaturas):
       super().__init__(nombre, edad, DNI)
       self.universidad = universidad
       self.curso = curso
       self.asignaturas = asignaturas 
    
    def describirse(self):
        print(f"Hola! Soy {self.nombre} tengo {self.edad} y estudio en la universidad {self.universidad}. Estoy en el curso {self.curso}.")


juan = Trabajador("Juan", 33, "45567345J", 1500, "jefe", "Google" )
juan.presentarse()
print(juan.DNI)
juan.calcular_sueldo_anual()
print(juan.calcular_sueldo_anual())
