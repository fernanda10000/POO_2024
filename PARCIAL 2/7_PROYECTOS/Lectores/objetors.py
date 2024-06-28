class Lectores:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def reservar(self):
        print(f"{self.nombre} ha reservado un libro.")

    def entregar(self):
        print(f"{self.nombre} ha entregado un libro.")


class Estudiantes(Lectores):
    def __init__(self, nombre, direccion, tel, carrera, matricula):
        super().__init__(nombre, direccion, tel)
        self.carrera = carrera
        self.matricula = matricula


class Docentes(Lectores):
    def __init__(self, nombre, direccion, tel, modalidad, num_empleado):
        super().__init__(nombre, direccion, tel)
        self.modalidad = modalidad
        self.num_empleado = num_empleado


# Crear instancias de Estudiantes y Docentes
estudiante1 = Estudiantes(
    nombre="Ana Torres Guzmán",
    direccion="Col. Centro 1500",
    tel="6181234567",
    carrera="MECA",
    matricula="2335678"
)

docente1 = Docentes(
    nombre="Daniel Fuentes Loera",
    direccion="Fracc. D. Arieta 1400",
    tel="6183375587",
    modalidad="TT",
    num_empleado="123"
)

# Imprimir detalles de los objetos creados
print("Detalles del estudiante:")
print(f"Nombre: {estudiante1.nombre}")
print(f"Dirección: {estudiante1.direccion}")
print(f"Teléfono: {estudiante1.tel}")
print(f"Carrera: {estudiante1.carrera}")
print(f"Matrícula: {estudiante1.matricula}")

print("\nDetalles del docente:")
print(f"Nombre: {docente1.nombre}")
print(f"Dirección: {docente1.direccion}")
print(f"Teléfono: {docente1.tel}")
print(f"Modalidad: {docente1.modalidad}")
print(f"Número de empleado: {docente1.num_empleado}")

# Demostración de métodos
print("\nAcciones del estudiante:")
estudiante1.reservar()
estudiante1.entregar()

print("\nAcciones del docente:")
docente1.reservar()
docente1.entregar()