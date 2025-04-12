# gestor_memoria.py

def worst_fit(memory, requirement, index_inicial):
    print("=" * 50)
    print("INICIANDO ASIGNACIÓN WORST FIT CIRCULAR")
    print("=" * 50)
    print(f"Requisito del proceso: {hex(requirement)} ({requirement} bytes)")
    print(f"Índice inicial de búsqueda: {index_inicial}")

    n = len(memory)

    if n == 0:
        print("\n[ERROR] No hay bloques de memoria disponibles.")
        print("=" * 50 + "\n")
        return None

    print("\nESTADO INICIAL DE LA MEMORIA:")
    for i in range(n):
        base, limite = memory[i]
        print(f"  Bloque {i}: Base = {hex(base)} ({base}), Límite = {hex(limite)} ({limite})")

    mejor_index = -1
    mayor_espacio = -1

    print("\nBUSCANDO EL BLOQUE CON MÁS ESPACIO DISPONIBLE...")

    for i in range(n):
        idx = (index_inicial + i) % n
        base, limite = memory[idx]

        print(f"  Revisando bloque {idx}: Límite disponible = {hex(limite)} ({limite})")

        if limite >= requirement:
            print(f"    Suficiente para el proceso (requiere {hex(requirement)} bytes)")
            if limite > mayor_espacio:
                mejor_index = idx
                mayor_espacio = limite
                print(f"    Nuevo candidato WORST FIT -> Bloque {idx} (espacio disponible: {hex(limite)} bytes)")

    if mejor_index == -1:
        print("\nNo se encontró un bloque suficientemente grande.")
        print("=" * 50 + "\n")
        return None

    print(f"\nBloque seleccionado para la asignación: Bloque {mejor_index}")

    base_asignado, limite_asignado = memory[mejor_index]
    base_retorno = base_asignado

    nuevo_base = base_asignado + requirement
    nuevo_limite = limite_asignado - requirement
    memory[mejor_index] = (nuevo_base, nuevo_limite)

    print("\nESTADO FINAL DE LA MEMORIA DESPUÉS DE LA ASIGNACIÓN:")
    for i in range(n):
        base, limite = memory[i]
        print(f"  Bloque {i}: Base = {hex(base)} ({base}), Límite = {hex(limite)} ({limite})")

    print("\nASIGNACIÓN COMPLETA")
    print("Resultado de la asignación:")
    print(f"  Dirección base asignada: {hex(base_retorno)} ({base_retorno})")
    print(f"  Tamaño del proceso: {hex(requirement)} ({requirement} bytes)")
    print(f"  Índice del bloque asignado: {mejor_index}")

    print("=" * 50 + "\n")

    return memory, base_retorno, requirement, mejor_index


if __name__ == "__main__":
    print("GESTOR DE MEMORIA - WORST FIT CIRCULAR\n")

    # Ejemplo de bloques de memoria disponibles
    work_memory = [
        (0x00A00000, 0x000C0000),  # Bloque 0
        (0x00B00000, 0x00080000),  # Bloque 1
        (0x00C00000, 0x000E0000)   # Bloque 2
    ]

    # Proceso que queremos asignar
    requirement = 0x000A0000  # 10 bloques (hex)
    index_inicial = 1

    resultado = worst_fit(work_memory, requirement, index_inicial)

    if resultado:
        memory, base_retorno, requirement, mejor_index = resultado
        print(f"\nProceso asignado en {hex(base_retorno)} ({base_retorno}) (bloque {mejor_index})")
        print("\nEstado final de la memoria:")
        for i in range(len(memory)):
            base, limite = memory[i]
            print(f"  Bloque {i}: Base = {hex(base)} ({base}), Límite = {hex(limite)} ({limite})")
    else:
        print("\nNo se pudo asignar el proceso.")
