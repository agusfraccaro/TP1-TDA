
def pd_entrenamientos(si, ei):

    soluciones = [([0] * len(ei)) for _ in range(len(ei))]

    for dias_disponibles_para_entrenar in range(1, len(ei) + 1):

        for dias_seguidos_entrenando in range(0, len(si)):

            if (dias_seguidos_entrenando > dias_disponibles_para_entrenar-1):
                break

            ganancia_para_energia_actual = min(
                # -1 porque el for de dias disponibles esta numerado de 1..n
                ei[dias_disponibles_para_entrenar - 1],
                si[dias_seguidos_entrenando]
            )

            ganancia_anterior = 0

            if dias_seguidos_entrenando == 0:
                if (dias_disponibles_para_entrenar > 2):
                    # -3 porque los fors estan numerados de 1..n
                    ganancia_anterior = max(soluciones[dias_disponibles_para_entrenar - 3])

            else:
                # -2 porque los fors estan numerados de 1..n
                ganancia_anterior = soluciones[dias_disponibles_para_entrenar - 2][dias_seguidos_entrenando - 1]

            ganancia = ganancia_anterior + ganancia_para_energia_actual
            soluciones[dias_disponibles_para_entrenar-1][dias_seguidos_entrenando] = ganancia

    return soluciones