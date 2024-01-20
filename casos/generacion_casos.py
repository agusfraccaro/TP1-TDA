import random
from typing import List, Tuple


def generar_tamanios():
    return [2 ** n for n in range(1, 10)]


def generar_tiempos_n_rivales(n: int) -> List[Tuple[int, int]]:
    return [(random.randint(1, 100), random.randint(1, 100)) for _i in range(n)]


def generar_casos(tamanios: List[int]):
    random.seed(42)
    return [generar_tiempos_n_rivales(n) for n in tamanios]
