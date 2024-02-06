
def imprimir_matriz(matriz):

    print("La matriz solución es: ")
    s = [[str(elemento) for elemento in fila] for fila in matriz]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)

    tabla = [fmt.format(*fila) for fila in s]
    print('\n'.join(tabla))