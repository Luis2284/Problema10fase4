# =============================================
# Nombre del estudiante: Luis Navarro Masson 
# Grupo: 81
# Problema 10 - Registro de estudiantes deportistas UNAD
# Código fuente: autoría propia
# =============================================

# Diccionario de selecciones deportivas
SELECCIONES = {
    1015: "FÚTBOL",
    1030: "BASKETBALL",
    1045: "CICLISMO"
}

def llenar_matriz(n=100):
    """Llena la matriz con los datos de los deportistas"""
    matriz = []
    print("Registro de deportistas UNAD\n")
    for i in range(n):
        print(f"--- Deportista #{i + 1} ---")
        
        # Validar cédula
        cedula = input("Cédula: ")
        while not cedula.isdigit() or int(cedula) <= 0:
            print("Ingrese una cédula válida (número positivo).")
            cedula = input("Cédula: ")
        cedula = int(cedula)

        # Validar sexo
        while True:
            try:
                sexo = int(input("Sexo (1. Mujer, 2. Hombre): "))
                if sexo in [1, 2]:
                    break
                else:
                    print("Debe ingresar 1 (Mujer) o 2 (Hombre).")
            except ValueError:
                print("Debe ingresar un número válido.")

        # Validar edad
        edad = input("Edad: ")
        while not edad.isdigit() or int(edad) <= 0:
            print("Ingrese una edad válida (número positivo).")
            edad = input("Edad: ")
        edad = int(edad)

        # Validar código de selección
        while True:
            try:
                cod_sel = int(input("Código de selección (1015, 1030, 1045): "))
                if cod_sel in SELECCIONES:
                    break
                else:
                    print("Código inválido. Debe ser 1015, 1030 o 1045.")
            except ValueError:
                print("Debe ingresar un número válido.")

        matriz.append([cedula, sexo, edad, cod_sel])
        print("-" * 50)
    return matriz

def mostrar_matriz(matriz):
    """Muestra todos los registros"""
    print("\nListado de deportistas registrados:")
    print("CÉDULA\tSEXO\tEDAD\tSELECCIÓN")
    for fila in matriz:
        sexo_str = "MUJER" if fila[1] == 1 else "HOMBRE"
        seleccion = SELECCIONES.get(fila[3], "DESCONOCIDA")
        print(f"{fila[0]}\t{sexo_str}\t{fila[2]}\t{seleccion}")
    print(f"\nTotal de deportistas registrados: {len(matriz)}")

def porcentaje_sexo(matriz):
    """Calcula y muestra el porcentaje de hombres y mujeres"""
    total = len(matriz)
    mujeres = sum(1 for fila in matriz if fila[1] == 1)
    hombres = total - mujeres
    p_mujeres = (mujeres / total) * 100
    p_hombres = (hombres / total) * 100
    print("\nPorcentajes de sexo:")
    print(f"Mujeres: {p_mujeres:.2f}%")
    print(f"Hombres: {p_hombres:.2f}%")

def deportistas_por_seleccion(matriz):
    """Cuenta cuántos deportistas hay por selección"""
    conteo = {codigo: 0 for codigo in SELECCIONES}
    for fila in matriz:
        if fila[3] in conteo:
            conteo[fila[3]] += 1
    print("\nCantidad de deportistas por selección:")
    for codigo, cantidad in conteo.items():
        print(f"{SELECCIONES[codigo]}: {cantidad}")

def main():
    # Para pruebas se puede usar n=5, para entrega oficial usar n=100
    matriz = llenar_matriz(5)
    mostrar_matriz(matriz)
    porcentaje_sexo(matriz)
    deportistas_por_seleccion(matriz)

if __name__ == "__main__":
    main()
