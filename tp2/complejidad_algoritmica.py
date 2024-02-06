import random
import time
import matplotlib.pyplot as plt

from casos.generar_casos import generar_caso
from tp2.algoritmo_resolucion import pd_entrenamientos, pd_reconstruccion


def generar_casos(tamanios):
    casos = [generar_caso(tamanio) for tamanio in tamanios]
    ei_si = []
    for caso in casos:
        ei_si.append((list(map(lambda x: x[0], caso)), list(map(lambda x: x[1], caso))))

    return ei_si


def normalizar(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data


def generar_grafico(tamanios, t, n_al_cuadrado, titulo, label, nombre_archivo):
    plt.figure()
    plt.plot(tamanios, t, marker='o', label=label, linewidth=0.5, markersize=2)
    plt.plot(tamanios, n_al_cuadrado, marker='o', label='n^2', linewidth=0.5, markersize=2)
    plt.xlabel('Tamaño del set de datos (N)')
    plt.title(titulo)
    plt.legend()
    plt.savefig(nombre_archivo)


def main():
    random.seed(42)

    tamanios = range(2, 2 ** 11, 16)
    #tamanios = range(2, 2 ** 9, 16)

    casos = generar_casos(tamanios)
    t_total = []
    t_entrenamientos = []
    t_reconstruccion = []
    n_al_cuadrado = normalizar([n ** 2 for n in tamanios])
    for caso in casos:
        start = time.time()
        soluciones = pd_entrenamientos(caso[1], caso[0])
        t_entrenamientos.append(time.time() - start)

        start_reconstruccion = time.time()
        pd_reconstruccion(soluciones)
        t_reconstruccion.append(time.time() - start_reconstruccion)

        t_total.append(time.time() - start)

    t_total = normalizar(t_total)
    t_entrenamientos = normalizar(t_entrenamientos)
    t_reconstruccion = normalizar(t_reconstruccion)

    generar_grafico(tamanios, t_total, n_al_cuadrado, 'Complejidad algorítmica total', 'Tiempo de ejecución total',
                    'graficos/complejidad_total.png')
    generar_grafico(tamanios, t_reconstruccion, n_al_cuadrado, 'Complejidad algorítmica reconstrucción de la solución',
                    'Tiempo de ejecución reconstrucción', 'graficos/complejidad_reconstruccion.png')
    generar_grafico(tamanios, t_entrenamientos, n_al_cuadrado, 'Complejidad algorítmica solución',
                    'Tiempo de ejecución entrenamientos', 'graficos/complejidad_entrenamientos.png')


if __name__ == '__main__':
    main()
