import random
from typing import List, Tuple

TAMANIO_BASICO = 10
TAMANIO_EXPANDIDO = 100

def _generar_tamanios():
    return [2 ** n for n in range(1, 100)]


def generar_tamanios():
    return _generar_tamanios(TAMANIO_BASICO)


def generar_tamanios_expandido():
    return _generar_tamanios(TAMANIO_EXPANDIDO)


def generar_tamanios_comparacion():
    return [3, 50, 1500, 250000]


def generar_tiempos_n_rivales(n: int) -> List[Tuple[int, int]]:
    return [(random.randint(1, 100), random.randint(1, 100)) for _i in range(n)]


def generar_casos(tamanios: List[int]):
    random.seed(42)
    return [generar_tiempos_n_rivales(n) for n in tamanios]
