
def pd_entrenamientos(si, ei):

    soluciones = [([0] * len(ei)) for i in range(len(ei))]

    for cantidad_dias_disponibles in range(1, len(ei) + 1):

        for dia_de_entrenamiento in range(1, len(si) + 1):

            if (dia_de_entrenamiento > cantidad_dias_disponibles):
                break

            # -1 porque los fors estan numerados de 1..n
            ganancia_que_puedo_obtener_para_mi_energia = min(ei[cantidad_dias_disponibles - 1], si[dia_de_entrenamiento - 1])

            ganancia_anterior = 0

            if dia_de_entrenamiento == 1:
                if (cantidad_dias_disponibles > 2):
                    # -3 porque los fors estan numerados de 1..n
                    ganancia_anterior = max(obtener_columna(soluciones, cantidad_dias_disponibles-3))

            else:
                # -2 porque los fors estan numerados de 1..n
                ganancia_anterior = soluciones[dia_de_entrenamiento - 2][cantidad_dias_disponibles - 2]

            ganancia = ganancia_anterior + ganancia_que_puedo_obtener_para_mi_energia
            soluciones[dia_de_entrenamiento - 1][cantidad_dias_disponibles - 1] = ganancia

    return soluciones

def obtener_columna(matriz, numero_columna):
    return [fila[numero_columna] for fila in matriz]