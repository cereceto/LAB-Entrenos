from collections import namedtuple
import csv
from datetime import datetime



Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_ficheros(fichero):
    with open(fichero, encoding = 'utf-8') as f:
        res = []
        lector = csv.reader(f)
        next(lector)
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector:
            tipo = str(tipo)
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            compartido = parsea_booleano(compartido)
            res.append(Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido))
        return res        
    
def parsea_booleano(cadena):
    if cadena == 'S':
        return True
    else:
        return False

def tipos_entrenos(entrenos):
    res = []
    for entreno in entrenos:
        if entreno.tipo not in res:
            res.append(entreno.tipo)
    return sorted(res)

def entrenos_duracion_superior(entrenos, d):
    res = []
    for entreno in entrenos:
        if entreno.duracion > d:
            res.append(entreno)
    return res

def suma_calorias(entrenos, f_inicio, f_fin):
    res = 0
    for entreno in entrenos:
        if f_inicio <= entreno.fechahora <= f_fin:
            res += entreno.calorias
    return res
        