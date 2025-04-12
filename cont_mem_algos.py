def worst_fit(memory, requirement, index_inicial):
    n = len(memory)

    if n == 0:
        return None

    mejor_index = -1
    mayor_espacio = -1

    for i in range(n):
        idx = (index_inicial + i) % n
        base, limite = memory[idx]

        if limite >= requirement:
            if limite > mayor_espacio:
                mejor_index = idx
                mayor_espacio = limite

    if mejor_index == -1:
        return None

    base_asignado, limite_asignado = memory[mejor_index]
    base_retorno = base_asignado

    nuevo_base = base_asignado + requirement
    nuevo_limite = limite_asignado - requirement
    memory[mejor_index] = (nuevo_base, nuevo_limite)

    return memory, base_retorno, requirement, mejor_index
