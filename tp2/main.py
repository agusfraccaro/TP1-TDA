from algoritmo_resolucion import pd_entrenamientos
from utilidades.utils import imprimir_matriz

SI = [10, 8, 6, 4, 2, 1]
EI = [2, 5, 3, 6, 8, 2]

SI2 = [63,61,49,41,40,38,23,17,13,10]
EI2 = [36,2,78,19,59,79,65,64,33,41]

EI3 = [67,8,12,34,6]
SI3 = [76,47,39,22,10]


def main():
    soluciones = pd_entrenamientos(SI3, EI3)

    imprimir_matriz(soluciones)

if __name__ == "__main__":
    main()
