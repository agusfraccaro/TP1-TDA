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
    N = range(2, 30)
    tamanios = [(n, math.floor(n / 2)) for n in N]
    cantidad_experimentos = 200
    probabilidades = [0.1, 0.5, 1]
    sets = [generar_experimentos(tamanios, cantidad_experimentos, p) for p in probabilidades]

    t_bt = []
    t_gr = []
    t_n_m_2_power_n = normalizar([n * (math.floor(n / 2)) * 2 ** n for n in N])
    t_n_power_2 = normalizar([(n ** 2) for n in N])

    for experimentos in sets:
        _t_bt = []
        _t_gr = []
        for experimento in experimentos:
            _t_bt_sum = 0
            _t_gr_sum = 0
            for caso in experimento:
                t_start = time.time()
                jugadores_prensa(caso, [], 0, [])
                t_end = time.time()
                _t_bt_sum += t_end - t_start

                t_start = time.time()
                jugadores_prensa_greedy(caso)
                t_end = time.time()
                _t_gr_sum += t_end - t_start

            _t_bt.append(_t_bt_sum / len(experimento))
            _t_gr.append(_t_gr_sum / len(experimento))

        _t_bt = normalizar(_t_bt)
        _t_gr = normalizar(_t_gr)
        t_bt.append(_t_bt)
        t_gr.append(_t_gr)

    generar_grafico(
        N,
        [t for t in t_bt] + [t_n_m_2_power_n],
        [f'p={i}' for i in probabilidades] + ['n*m*2^n'],
        'Complejidad algorítmica backtracking',
        'complejidad_algoritmica_backtracking.png'
    )

    generar_grafico(
        N,
        [t for t in t_gr] + [t_n_power_2],
        [f'p={i}' for i in probabilidades] + ['n^2'],
        'Complejidad algorítmica greedy',
        'complejidad_algoritmica_greedy.png'
    )


def comparar_resultados():
    tamanios = [(30, 15)]
    cantidad_experimentos = 21
    probabilidad = 0.3
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
