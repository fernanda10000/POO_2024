class Lectores:
    def _init_(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def reservar(self):
        print(f"{self.nombre} ha reservado un libro.")

    def entregar(self):
        print(f"{self.nombre} ha entregado un libro.")


class Estudiantes(Lectores):
    def _init_(self, nombre, direccion, tel, carrera, matricula):
        super()._init_(nombre, direccion, tel)
        self.carrera = carrera
        self.matricula = matricula


class Docentes(Lectores):
    def _init_(self, nombre, direccion, tel, modalidad, num_empleado):
        super()._init_(nombre, direccion, tel)
        self.modalidad = modalidad
        self.num_empleado = num_empleado


# Crear instancias de Estudiantes y Docentes
estudiante1 = Estudiantes("Ana Torres Guzmán", "Col. Centro 1500", "6181234567", "MECA", "2335678")
docente1 = Docentes("Daniel Fuentes Loera", "Fracc. D. Arieta 1400", "6183375587", "TT", "123")

# Demostración de métodos
estudiante1.reservar()
estudiante1.entregar()
docente1.reservar()
docente1.entregar()




