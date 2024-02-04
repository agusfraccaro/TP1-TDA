import csv
import random
import sys

def generar_csv(nombre_archivo, tamanio):
    e_i = [random.randint(1, tamanio*2) for _ in range(tamanio)]

    # Generar datos aleatorios únicos para S_i
    s_i_unicos = random.sample(range(1, tamanio*2), tamanio)
    s_i_unicos.sort(reverse=True)
    # Ordenar por S_i de forma descendente
    datos = sorted(zip(e_i, s_i_unicos), key=lambda x: x[1], reverse=True)

    # Crear archivo CSV
    with open(nombre_archivo, 'w', newline='') as csvfile:
        fieldnames = ['E_i', 'S_i']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for dato in datos:
            writer.writerow({'E_i': dato[0], 'S_i': dato[1]})

def main():
    if len(sys.argv) != 3:
        print("Uso: python3 generar_casos.py <nombre_archivo.csv> <tamanio>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    tamanio = int(sys.argv[2])

    generar_csv(nombre_archivo, tamanio)

main()