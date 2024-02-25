# Verifica si la solución contenta a todos los periodistas
def es_eleccion_valida(solucion, pedidos_prensa):
    for pedido in pedidos_prensa:
        if not any(jugador in pedido for jugador in solucion):
            return False
    return True

# Verifica si el pedido de una prensa está en la solución
def esta_en_solucion(pedido, solucion):
    return any(jugador in pedido for jugador in solucion)

# Obtiene el conjunto mínimo de jugadores para satisfacer a toda la prensa
def jugadores_prensa(pedidos_prensa, sol_parcial, i, mejor_solucion):
    if len(mejor_solucion) > 0 and len(sol_parcial) == len(mejor_solucion):
        return False
    
    pedido_actual = pedidos_prensa[i]

    if esta_en_solucion(sol_parcial, pedido_actual):
        return jugadores_prensa(pedidos_prensa, sol_parcial, i + 1, mejor_solucion)
    
    cant_jugadores = len(sol_parcial)
    cant_solucion = len(mejor_solucion)
    for jugador in pedido_actual:
        if cant_solucion > 0 and cant_jugadores + 1 >= cant_solucion:
            return True
        
        sol_parcial.append(jugador)
        cant_jugadores += 1

        if es_eleccion_valida(sol_parcial, pedidos_prensa[i:]):
            mejor_solucion[:] = sol_parcial
            cant_solucion = cant_jugadores
        else:
            valido = jugadores_prensa(pedidos_prensa, sol_parcial, i + 1, mejor_solucion)
            if not valido:
                sol_parcial.pop()
                break 
        sol_parcial.pop()
        cant_jugadores -= 1

    return True
    

