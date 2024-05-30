def main():
    aprobados = 0
    reprobados = 0
    for i in range(15):
        calificacion = float(input(f"Introduce la calificación del alumno {i+1}: "))
        if calificacion >= 60:
            aprobados += 1
        else:
            reprobados += 1

    print(f"Alumnos aprobados: {aprobados}")
    print(f"Alumnos reprobados: {reprobados}")

if __name__ == "__main__":
    main()