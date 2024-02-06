import random
import time

from casos.generar_casos import generar_caso
from tp2.algoritmo_resolucion import pd_entrenamientos, pd_reconstruccion


def generar_casos():
    tamanios = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    casos = [generar_caso(tamanio) for tamanio in tamanios]
    ei_si = []
    for caso in casos:
        ei_si.append((list(map(lambda x: x[0], caso)), list(map(lambda x: x[1], caso))))

    return ei_si

def main():
    random.seed(42)
    casos = generar_casos()
    t_total = []
    t_entrenamientos = []
    t_reconstruccion = []
    for caso in casos:
        start = time.time()
        soluciones = pd_entrenamientos(caso[1], caso[0])
        t_entrenamientos.append(time.time() - start)

        start_reconstruccion = time.time()
        pd_reconstruccion(soluciones)
        t_reconstruccion.append(time.time() - start_reconstruccion)

        t_total.append(time.time() - start)

    print(t_total)
    print(t_entrenamientos)
    print(t_reconstruccion)


if __name__ == '__main__':
    main()
