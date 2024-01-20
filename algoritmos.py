from typing import List, Tuple, Callable


def greedy_scaloni_por_ayudante(tiempos: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :return: lista de ordenada por A_i en orden descendiente
    """
    return sorted(tiempos, key=lambda t: t[1], reverse=True)


def greedy_scaloni_por_diferencia(tiempos: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :return: lista de ordenada por A_i - S_i en orden descendiente
    """
    return sorted(tiempos, key=lambda t: t[1] - t[0], reverse=True)


def greedy_scaloni_por_scaloni(tiempos: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :return: lista de ordenada por S_i en orden ascendente
    """
    return sorted(tiempos, key=lambda t: t[0])


def calcular_tiempo_analisis(tiempos: List[Tuple[int, int]]) -> int:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :return: tiempo final que tomara analizar todos los casos
    """
    t_scaloni = 0
    t_final = 0
    for tiempo in tiempos:
        t_scaloni += tiempo[0]
        t_final = max(t_final, t_scaloni + tiempo[1])
    return t_final


def calcular_tiempo_analisis_completo(tiempos: List[Tuple[int, int]], algoritmo: Callable) -> int:
    """
    :param tiempos: lista de tuplas con los tiempos de Scaloni y ayudante (S_i, A_i)
    :param algoritmo: algoritmo de ordenamiento utilizado para el calculo del menor tiempo
    :return: tiempo final que tomara analizar todos los casos
    """
    tiempos_ordenados = algoritmo(tiempos)
    return calcular_tiempo_analisis(tiempos_ordenados)


ALGORITMOS = {"ayudante": greedy_scaloni_por_ayudante,
              "diferencia": greedy_scaloni_por_diferencia,
              "scaloni": greedy_scaloni_por_scaloni}
