import argparse

from algoritmo_backtracking import jugadores_prensa
from algoritmo_greedy import (jugadores_prensa_greedy)


def parsear_argumentos():
    """
    :return: path del archivo
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Ruta al archivo de tiempos", required=True)
    args = parser.parse_args()
    path = args.path

    return path

def cargar_datos(path: str):
    """
    :param path: path del archivo con las listas de la prensa
    :return: lista de listas, donde cada lista son los jugadores elegidos por cada prensa
    """
    with open(path, 'r') as archivo:
        lineas = archivo.readlines()

    pedidos_prensa = []

    for linea in lineas:
        pedidos_prensa.append(linea.strip().split(','))

    return pedidos_prensa

def main():
    path = parsear_argumentos()
    pedidos_prensa = cargar_datos(path)

    print(f"Pedidos de la prensa: {pedidos_prensa}")

    solucion_bt = []
    jugadores_prensa(pedidos_prensa, [], 0, solucion_bt)
    solucion_greedy = jugadores_prensa_greedy(pedidos_prensa)
    print(f"Mejor solución bt: {solucion_bt}")
    print(f"Mejor solución greedy: {solucion_greedy}")

if __name__ == "__main__":
    main()
