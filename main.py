import argparse
import time
from typing import List, Tuple, Callable

from algoritmos import ALGORITMOS, calcular_tiempo_analisis


def cargar_tiempos(path: str) -> List[Tuple[int, int]]:
    """
    :param path: path del archivo con los tiempos en formato Si,Ai
    :return: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    """
    with open(path, "r") as archivo:
        lineas = archivo.readlines()
        tiempos = []
        for linea in lineas[1:]:
            t_i = linea.strip().split(',')
            s_i = int(t_i[0])
            a_i = int(t_i[1])
            tiempos.append((s_i, a_i))

    return tiempos


def parsear_argumentos() -> Tuple[str, Callable[[List[Tuple[int, int]]], List[Tuple[int, int]]]]:
    """
    :return: tupla con el path del archivo y la funcion del algoritmo a utilizar
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Ruta al archivo de tiempos", required=True)
    parser.add_argument("-a", "--algoritmo",
                        help="Algoritmo a utilizar",
                        choices=["ayudante", "diferencia", "scaloni"],
                        default="ayudante")
    args = parser.parse_args()
    path = args.path
    algoritmo = ALGORITMOS[args.algoritmo]

    return path, algoritmo

def main():
    path, algoritmo = parsear_argumentos()

    tiempos = cargar_tiempos(path)
    print("Archivo {} cargado correctamente con n={}".format(path, len(tiempos)))

    print("Utilizando algoritmo {}".format(algoritmo.__name__))
    t_i = time.time()
    tiempos_ordenados = algoritmo(tiempos)
    t_f = time.time()
    print("Tiempo de ejecucion: {} segundos".format(t_f - t_i))

    tiempo_analisis = calcular_tiempo_analisis(tiempos_ordenados)
    print("Tiempo final del analisis: {}".format(tiempo_analisis))

if __name__ == "__main__":
    main()
