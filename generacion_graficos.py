import random
import time
import math
from typing import List, Tuple
import matplotlib.pyplot as plt

from algoritmos import greedy_scaloni_por_ayudante


def generar_caso(n: int) -> List[Tuple[int, int]]:
    return [(random.randint(1, 100), random.randint(1, 100)) for _i in range(n)]


def normalizar(data):
    min_val = min(data)
    max_val = max(data)
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    return normalized_data


def main():
    random.seed(42)
    N = [2 ** n for n in range(1, 15)]
    casos = [generar_caso(n) for n in N]
    t = []
    nlogn = normalizar([n * math.log2(n) for n in N])
    for caso in casos:
        t_i = time.time()
        greedy_scaloni_por_ayudante(caso)
        t_f = time.time()
        t.append(t_f - t_i)

    t = normalizar(t)

    plt.plot(N, t, marker='o', label='Actual Time (s)')

    plt.plot(N, nlogn, marker='o', label='n * log2(n)')

    plt.xscale('log')
    plt.xlabel('Input Size (N)')
    plt.ylabel('Time (s) / n * log2(n)')
    plt.title('Time Complexity Analysis')
    plt.legend()
    plt.savefig('time_complexity_plot.png')


main()
