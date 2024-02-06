from algoritmo_resolucion import pd_entrenamientos, pd_reconstruccion
from utilidades.utils import imprimir_matriz
import argparse

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
    :param path: path del archivo con los tiempos en formato Ei,Si
    :return: lista de tuplas con las energias necesarias para los entrenamientos
    y la energia disponible en el dia de entrenamiento (E_i, S_i)
    """
    with open(path, "r") as archivo:
        lineas = archivo.readlines()
        energias = []
        esfuerzos = []
        for linea in lineas[1:]:
            t_i = linea.strip().split(',')
            esfuerzos.append(int(t_i[0]))
            energias.append(int(t_i[1]))

    return esfuerzos, energias

def main():
    path = parsear_argumentos()
    ei, si = cargar_datos(path)
    print(f"Si: {si}")
    print(f"Ei: {ei}")
    soluciones = pd_entrenamientos(si, ei)
    imprimir_matriz(soluciones)

    reconstruccion = pd_reconstruccion(soluciones)    
    print('Conjunto de dias optimos para entrenar:', reconstruccion)

if __name__ == "__main__":
    main()
