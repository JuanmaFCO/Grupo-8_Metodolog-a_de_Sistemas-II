from funciones.promedio_ituarte import promedio_ituarte

def test_promedio_ituarte_basico():
    assert promedio_ituarte([2, 4, 6]) == 4

def test_promedio_ituarte_lista_vacia():
    assert promedio_ituarte([]) is None

def test_promedio_ituarte_numeros_negativos():
    assert promedio_ituarte([-2, -4, -6]) == -4

def test_promedio_ituarte_decimales():
    assert promedio_ituarte([1, 2]) == 1.5
