
# Cuenta la cantidad de veces que aparece cada jugador en un subjconjunto y lo almacena en un diccionario
def agrupar_por_apariciones(pedidos_prensa):
    apariciones_por_jugador = {}

    for pedido in pedidos_prensa:
        for jugador in pedido:
            if jugador not in apariciones_por_jugador:
                apariciones_por_jugador[jugador] = 1
            else:
                apariciones_por_jugador[jugador] += 1

    return apariciones_por_jugador


# Inicializa un listado que mantiene la informacion de si un pedido ya fue mapeado.
def mapear_pedidos_cubiertos(pedidos_prensa):
    pedidos_mapeados = []
    for pedido in pedidos_prensa:
        pedidos_mapeados.append([False, pedido])

    return pedidos_mapeados


def actualizar_pedidos_cubiertos_por_jugador(pedidos_cubiertos, jugador):
    nuevos_pedidos_cubiertos = 0

    #print(pedidos_cubiertos)
    for idx in range(len(pedidos_cubiertos)):
        if pedidos_cubiertos[idx][0]:
            continue

        if jugador in pedidos_cubiertos[idx][1]:
            pedidos_cubiertos[idx][0] = True
            nuevos_pedidos_cubiertos += 1

    return nuevos_pedidos_cubiertos


def jugadores_prensa_greedy(pedidos_prensa):

    if len(pedidos_prensa) == 0:
        return []

    apariciones_por_jugador = agrupar_por_apariciones(pedidos_prensa)
    pedidos_cubiertos = mapear_pedidos_cubiertos(pedidos_prensa)

    pedidos_sin_cubrir = len(pedidos_prensa)

    solucion = []

    for _ in range(len(apariciones_por_jugador.values())):

        if pedidos_sin_cubrir == 0:
            break

        jugador_con_mas_apariciones = max(apariciones_por_jugador, key=apariciones_por_jugador.get)
        pedidos_cubiertos_con_nuevo_jugador = actualizar_pedidos_cubiertos_por_jugador(
            pedidos_cubiertos, jugador_con_mas_apariciones
        )

        pedidos_sin_cubrir -= pedidos_cubiertos_con_nuevo_jugador
        solucion.append(jugador_con_mas_apariciones)
        apariciones_por_jugador.pop(jugador_con_mas_apariciones)

    return solucion
