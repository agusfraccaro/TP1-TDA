import math
import random
import time

from matplotlib import pyplot as plt

from tp3.algoritmo_backtracking import jugadores_prensa
from tp3.algoritmo_greedy import jugadores_prensa_greedy


def generar_caso(cantidad_jugadores, cantidad_conjuntos, probabilidad):
    return [[f'Jugador {i}' for i in range(cantidad_jugadores) if random.random() < probabilidad] for _ in
            range(cantidad_conjuntos)]


def generar_experimentos(tamanios, cantidad_experimentos, probabilidad):
    experimentos = []
    for (cantidad_jugadores, cantidad_conjuntos) in tamanios:
        experimentos.append(
            [generar_caso(cantidad_jugadores, cantidad_conjuntos, probabilidad) for _ in range(cantidad_experimentos)]
        )
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


def comparar_complejidad():
    N = range(2, 75)
    tamanios = [(n, math.floor(n / 2)) for n in N]
    cantidad_experimentos = 40
    probabilidad = 0.5
    experimentos = generar_experimentos(tamanios, cantidad_experimentos, probabilidad)

    t_bt = []
    t_gr = []
    for experimento in experimentos:
        _t_bt = 0
        _t_gr = 0
        for caso in experimento:
            t_start = time.time()
            jugadores_prensa(caso, [], 0, [])
            t_end = time.time()
            _t_bt += t_end - t_start

            t_start = time.time()
            jugadores_prensa_greedy(caso)
            t_end = time.time()
            _t_gr += t_end - t_start

        t_bt.append(_t_bt / len(experimento))
        t_gr.append(_t_gr / len(experimento))

    t_bt = normalizar(t_bt)
    t_gr = normalizar(t_gr)

    generar_grafico(
        N,
        [t_bt, t_gr],
        ['Backtracking', 'Greedy'],
        'Complejidad algorítmica',
        'complejidad_algoritmica.png'
    )


def comparar_resultados():
    tamanios = [(20, 10)]
    cantidad_experimentos = 10
    probabilidad = 0.15
    experimentos = generar_experimentos(tamanios, cantidad_experimentos, probabilidad)

    soluciones_bt = []
    soluciones_gr = []
    for experimento in experimentos:
        for caso in experimento:
            bt = []
            jugadores_prensa(caso, [], 0, bt)
            soluciones_bt.append(len(bt))
            soluciones_gr.append(len(jugadores_prensa_greedy(caso)))

    plt.figure()
    plt.plot(soluciones_bt, marker='o', label='Backtracking', linewidth=0.5, markersize=2)
    plt.plot(soluciones_gr, marker='o', label='Greedy', linewidth=0.5, markersize=2)
    plt.xlabel('Experimento')
    plt.ylabel('Cantidad de jugadores')
    plt.title('Comparación de resultados')
    plt.legend()
    plt.savefig('comparacion_resultados.png')


def main():
    # Complejidad
    comparar_complejidad()

    # Resultados
    comparar_resultados()


if __name__ == '__main__':
    main()
