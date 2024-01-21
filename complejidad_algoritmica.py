import math
import time

import matplotlib.pyplot as plt

from algoritmos import greedy_scaloni_por_ayudante
from casos.generacion_casos import generar_casos, generar_tamanios


def normalizar(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data


def main():
    tamanios = generar_tamanios()
    casos = generar_casos(tamanios)
    t = []
    nlogn = normalizar([n * math.log2(n) for n in tamanios])
    for caso in casos:
        t_i = time.time()
        greedy_scaloni_por_ayudante(caso)
        t_f = time.time()
        t.append(t_f - t_i)

    t = normalizar(t)

    plt.plot(tamanios, t, marker='o', label='Tiempo de ejecución')

    plt.plot(tamanios, nlogn, marker='o', label='n * log2(n)')

    plt.xscale('log')
    plt.xlabel('Tamaño del set de datos (N)')
    plt.title('Complejidad algorítmica')
    plt.legend()
    plt.savefig('graficos/time_complexity_plot.png')


main()
