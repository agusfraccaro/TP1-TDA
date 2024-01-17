import random
import time
from typing import List, Tuple
import matplotlib.pyplot as plt

from algoritmos import greedy_scaloni_por_ayudante


def generar_caso(n: int) -> List[Tuple[int, int]]:
    return [(random.randint(1, 100), random.randint(1, 100)) for _i in range(n)]


def main():
    random.seed(42)
    N = [2 ** n for n in range(1, 15)]
    casos = [generar_caso(n) for n in N]
    t = []
    for caso in casos:
        t_i = time.time()
        greedy_scaloni_por_ayudante(caso)
        t_f = time.time()
        t.append(t_f - t_i)

    plt.plot(N, t, marker='o')
    plt.xscale('log')
    plt.xlabel('Input Size (N)')
    plt.ylabel('Time (s)')
    plt.title('Time Complexity Analysis')
    plt.savefig('time_complexity_plot.png')


main()
