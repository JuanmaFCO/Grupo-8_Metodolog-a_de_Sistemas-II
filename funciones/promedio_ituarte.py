def promedio_ituarte(numeros):
    """
    Devuelve el promedio de una lista de números.
    Si la lista está vacía o es None, devuelve None.
    """
    if not numeros:
        return None
    return sum(numeros) / len(numeros)
