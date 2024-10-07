from entrenos import *

def test_lee_ficheros():
    print("Testeando lee_ficheros()... ")
    entrenos = lee_ficheros("WORKSPACE-LAB\LAB-Entrenos\data\entrenos.csv")
    print(f"Entrenos leídos: {len(entrenos)}")
    print("Primeros 3 entrenos:", entrenos[:3])
    print("Últimos 3 entrenos:", entrenos[-3:])
    print()

def test_parsea_booleano():
    print("Testeando parsea_booleano()... ")
    print(f"Resultado: {parsea_booleano('S')}")
    print(f"Resultado: {parsea_booleano('N')}")
    print()

def test_tipos_entrenos(entrenos):
    print("Testeando tipos_entrenos()... ")
    tipos = tipos_entrenos(entrenos)
    print(f"Tipos de entrenos: {tipos}")
    print()

def test_entrenos_duracion_superior(entrenos, duracion):
    print("Testeando entrenos_duracion_superior()... ")
    entrenos_superiores = entrenos_duracion_superior(entrenos, duracion)
    print(f"Entrenos con duración superior a {duracion} minutos: {len(entrenos_superiores)}")
    print()

def test_suma_calorias(entrenos, f_inicio, f_fin):
    print("Testeando suma_calorias()... ")
    calorias = suma_calorias(entrenos, f_inicio, f_fin)
    print(f"Calorías totales entre {f_inicio} y {f_fin}: {calorias}")
    print()

if __name__ == "__main__":

    entrenos = lee_ficheros("WORKSPACE-LAB\LAB-Entrenos\data\entrenos.csv")
    test_lee_ficheros()
    test_parsea_booleano()
    test_tipos_entrenos(entrenos)
    test_entrenos_duracion_superior(entrenos, 60)
    test_suma_calorias(entrenos, datetime(2021, 1, 1), datetime(2021, 12, 31))
