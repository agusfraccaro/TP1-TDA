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
    :param path: path del archivo con los tiempos en formato Si,Ai
    :return: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
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
    EI, SI = cargar_datos(path)
    print(SI)
    print(EI)
    soluciones = pd_entrenamientos(SI, EI)
    imprimir_matriz(soluciones)

    reconstruccion = pd_reconstruccion(soluciones)    
    print('Conjunto de dias optimos para entrenar:', reconstruccion)

if __name__ == "__main__":
    main()
