import math
import random
import time
import matplotlib.pyplot as plt

from casos.generar_casos import generar_caso
from tp2.algoritmo_resolucion import pd_entrenamientos, pd_reconstruccion


def generar_experimentos(tamanios, cantidad_experimentos):
    experimentos = []
    for tamanio in tamanios:
        casos = [generar_caso(tamanio) for _ in range(cantidad_experimentos)]
        ei_si = []
        for caso in casos:
            ei_si.append((list(map(lambda x: x[0], caso)), list(map(lambda x: x[1], caso))))
        experimentos.append(ei_si)

    return experimentos


def generar_peor_caso(tamanios):
    experimentos = []
    for tamanio in tamanios:
        ei = [tamanio * 10] * tamanio
        si = list(range(tamanio, 0, -1))
        si[0] = tamanio * 10
        experimentos.append([ei, si])

    return experimentos


def generar_mejor_caso(tamanios, cantidad_experimentos):
    experimentos = []
    for tamanio in tamanios:
        casos = [
            [[random.randint(1, tamanio) for _ in range(tamanio)], list(range(tamanio * 100, tamanio * 99, -1))]
            for _ in range(cantidad_experimentos)
        ]
        experimentos.append(casos)

    return experimentos


def normalizar(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data


def generar_grafico(tamanios, curves, labels, titulo, nombre_archivo):
    plt.figure()
    for curve, label in zip(curves, labels):
        plt.plot(tamanios, curve, marker='o', label=label, linewidth=0.5, markersize=2)
    plt.xlabel('Tamaño del set de datos (N)')
    plt.ylabel('Tiempo normalizado')
    plt.title(titulo)
    plt.legend()
    plt.savefig(nombre_archivo)


def complejidad_mejor_caso():
    tamanios = range(2, 2 ** 10, 8)
    experimentos = generar_mejor_caso(tamanios, 10)

    t_total = []
    t_entrenamientos = []
    t_reconstruccion = []

    for experimento in experimentos:
        _t_total = 0
        _t_entrenamientos = 0
        _t_reconstruccion = 0
        for caso in experimento:
            start = time.time()
            soluciones = pd_entrenamientos(caso[1], caso[0])
            _t_entrenamientos += time.time() - start
            start_reconstruccion = time.time()
            pd_reconstruccion(soluciones)
            end = time.time()
            _t_reconstruccion += end - start_reconstruccion
            _t_total += end - start

        t_total.append(_t_total / len(experimento))
        t_entrenamientos.append(_t_entrenamientos / len(experimento))
        t_reconstruccion.append(_t_reconstruccion / len(experimento))

    n_lineal = normalizar([n for n in tamanios])
    n_al_cuadrado = normalizar([n ** 2 for n in tamanios])
    t_reconstruccion = normalizar(t_reconstruccion)
    t_entrenamientos = normalizar(t_entrenamientos)
    t_total = normalizar(t_total)

    generar_grafico(tamanios, [t_reconstruccion, n_lineal], ['Complejidad algorítmica reconstrucción', 'n'],
                    'Tiempo de ejecución reconstrucción para el mejor caso',
                    'graficos/complejidad_reconstruccion_mejor_caso.png')
    generar_grafico(tamanios, [t_entrenamientos, n_al_cuadrado], ['Complejidad algorítmica entrenamientos', 'n^2'],
                    'Tiempo de ejecución entrenamientos para el mejor caso',
                    'graficos/complejidad_entrenamientos_mejor_caso.png')
    generar_grafico(tamanios, [t_total, n_al_cuadrado], ['Complejidad algorítmica total', 'n^2'],
                    'Tiempo de ejecución total para el mejor caso', 'graficos/complejidad_total_mejor_caso.png')


def complejidad_peor_caso():
    tamanios = range(2, 2 ** 10, 8)
    experimentos = generar_peor_caso(tamanios)

    t_total = []
    t_entrenamientos = []
    t_reconstruccion = []

    for caso in experimentos:
        start = time.time()
        soluciones = pd_entrenamientos(caso[1], caso[0])
        t_entrenamientos.append(time.time() - start)
        start_reconstruccion = time.time()
        pd_reconstruccion(soluciones)
        t_reconstruccion.append(time.time() - start_reconstruccion)
        t_total.append(time.time() - start)

    n_al_cuadrado = normalizar([n ** 2 for n in tamanios])
    t_reconstruccion = normalizar(t_reconstruccion)
    t_entrenamientos = normalizar(t_entrenamientos)
    t_total = normalizar(t_total)
    generar_grafico(tamanios, [t_reconstruccion, n_al_cuadrado], ['Complejidad algorítmica reconstrucción', 'n^2'],
                    'Tiempo de ejecución reconstrucción para el peor caso',
                    'graficos/complejidad_reconstruccion_peor_caso.png')
    generar_grafico(tamanios, [t_entrenamientos, n_al_cuadrado], ['Complejidad algorítmica entrenamientos', 'n^2'],
                    'Tiempo de ejecución entrenamientos para el peor caso',
                    'graficos/complejidad_entrenamientos_peor_caso.png')
    generar_grafico(tamanios, [t_total, n_al_cuadrado], ['Complejidad algorítmica total', 'n^2'],
                    'Tiempo de ejecución total para el peor caso', 'graficos/complejidad_total_peor_caso.png')


def main():
    complejidad_mejor_caso()
    return

    random.seed(42)
    tamanios = range(2, 2 ** 10, 8)
    experimentos = generar_experimentos(tamanios, 10)
    t_total = []
    t_entrenamientos = []
    t_reconstruccion = []
    n_al_cuadrado = normalizar([n ** 2 for n in tamanios])
    n_lineal = normalizar([n for n in tamanios])

    for experimento in experimentos:
        _t_total = 0
        _t_entrenamientos = 0
        _t_reconstruccion = 0
        for caso in experimento:
            start = time.time()
            soluciones = pd_entrenamientos(caso[1], caso[0])
            _t_entrenamientos += time.time() - start
            start_reconstruccion = time.time()
            pd_reconstruccion(soluciones)
            end = time.time()
            _t_reconstruccion += end - start_reconstruccion
            _t_total += end - start

        t_total.append(_t_total / len(experimento))
        t_entrenamientos.append(_t_entrenamientos / len(experimento))
        t_reconstruccion.append(_t_reconstruccion / len(experimento))

    t_total = normalizar(t_total)
    t_entrenamientos = normalizar(t_entrenamientos)
    t_reconstruccion = normalizar(t_reconstruccion)

    generar_grafico(
        tamanios,
        [t_total, n_al_cuadrado],
        ['Complejidad algorítmica total', 'n^2'],
        'Tiempo de ejecución total',
        'graficos/complejidad_total.png'
    )
    generar_grafico(
        tamanios,
        [t_entrenamientos, n_al_cuadrado],
        ['Complejidad algorítmica entrenamientos', 'n^2'],
        'Tiempo de ejecución entrenamientos',
        'graficos/complejidad_entrenamientos.png'
    )
    generar_grafico(
        tamanios, [t_reconstruccion, n_lineal, n_al_cuadrado],
        ['Complejidad algorítmica reconstrucción', 'n', 'n^2'],
        'Tiempo de ejecución reconstrucción',
        'graficos/complejidad_reconstruccion.png'
    )


if __name__ == '__main__':
    main()
