def jugador_esta_en_pedido(jugador, pedido):
    for jugador_pedido in pedido:
        if jugador_pedido == jugador:
            return True
    return False


def hitting_set_is_valid(pedidos_prensa, jugadores_elegidos):
    for pedido in pedidos_prensa:
        valido = False
        for jugador in jugadores_elegidos:
            if jugador_esta_en_pedido(jugador, pedido):
                valido = True
                break
        if not valido:
            print(f"El pedido: {pedido} no fue cubierto con los jugadores: {jugadores_elegidos}")
            return False

    print("Todos los pedidos fueron cubiertos")
    return True
