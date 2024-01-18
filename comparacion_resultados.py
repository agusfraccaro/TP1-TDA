import os
import time
from typing import List, Tuple
import numpy as np
import matplotlib.pyplot as plt

from algoritmos import ALGORITMOS, calcular_tiempo_analisis

DIRECTORIO_ARCHIVOS = "casos"

def cargar_tiempos(path: str) -> List[Tuple[int, int]]:
    with open(path, "r") as archivo:
        lineas = archivo.readlines()
        tiempos = []
        for linea in lineas[1:]:
            t_i = linea.strip().split(',')
            s_i = int(t_i[0])
            a_i = int(t_i[1])
            tiempos.append((s_i, a_i))
    return tiempos


def analizar_resultados_tiempo_analisis() -> None:
    archivos_csv = [archivo for archivo in os.listdir(DIRECTORIO_ARCHIVOS) if archivo.endswith(".csv")]

    nombre_algoritmos = list(ALGORITMOS.keys())
    colores = ['red', 'green', 'blue']
    bar_width = 0.2
    eje_x = np.arange(len(nombre_algoritmos))

    fig, axs = plt.subplots(len(archivos_csv), 1, figsize=(10, 7 * len(archivos_csv)))
    # Ajustar el espacio vertical entre subgráficos
    plt.subplots_adjust(hspace=0.6)

    # Calculo para cada archivo y ploteo:
    for i, archivo_csv in enumerate(archivos_csv):
        path = os.path.join(DIRECTORIO_ARCHIVOS, archivo_csv)
        tiempos = cargar_tiempos(path)

        print("Archivo {} cargado correctamente con n={}".format(archivo_csv, len(tiempos)))
        nombres_gr = []
        tiempos_gr = []

        for nombre, algoritmo in ALGORITMOS.items():
            tiempos_ordenados = algoritmo(tiempos.copy())
            resultado_analisis = calcular_tiempo_analisis(tiempos_ordenados)

            nombres_gr.append(nombre)
            tiempos_gr.append(resultado_analisis)

            print("Tiempo final del análisis para {} con {}: {}".format(archivo_csv, nombre, resultado_analisis))

        # Cargo grafico de barras
        bars = axs[i].bar(eje_x + i, tiempos_gr, width=bar_width, label=nombres_gr, color=colores)

        # Encontrar la barra con el menor valor
        min_bar = min(bars, key=lambda bar: bar.get_height())

        # Obtener la altura del rectángulo desde la base hasta la altura máxima de la barra
        rect_height = min_bar.get_height() - axs[i].get_ylim()[0]

        # Remarco el rectangulo con el menor valor.
        rect = plt.Rectangle((min_bar.get_x(), axs[i].get_ylim()[0]), min_bar.get_width(), rect_height, linewidth=3, edgecolor='y', facecolor='none')
        axs[i].add_patch(rect)

        # Agrego sobre cada barra su valor.
        for index, value in enumerate(tiempos_gr):
            axs[i].text(eje_x[index] + i, value, f'{value:.0f}', ha='center', va='bottom')

        axs[i].set_xlabel('Algoritmos', fontsize=10, weight='bold')
        axs[i].set_ylabel('Tiempo de Análisis (dias)', fontsize=10, weight='bold')

        # Customizo el eje y para setear limites y desactivar notacion cientifica
        axs[i].set_ylim(bottom=0, top=max(tiempos_gr) * 1.2)
        axs[i].ticklabel_format(axis='y', style='plain')

        axs[i].set_xticks(eje_x + i)
        axs[i].set_xticklabels(nombre_algoritmos)
        # Ajusto la posición de la leyenda
        axs[i].legend(bbox_to_anchor=(1.10, 0.5), loc='center right')
        axs[i].set_title('Comparación de Tiempo de Análisis para {}'.format(archivo_csv))
        axs[i].grid(True)

    plt.savefig('results_comparison_plot.png')
    plt.show()


def analizar_resultados_tiempo_ejecucion() -> None:
    archivos_csv = [archivo for archivo in os.listdir(DIRECTORIO_ARCHIVOS) if archivo.endswith(".csv")]

    nombre_algoritmos = list(ALGORITMOS.keys())
    colores = ['red', 'green', 'blue']
    bar_width = 0.2
    eje_x = np.arange(len(nombre_algoritmos))

    fig, axs = plt.subplots(len(archivos_csv), 1, figsize=(10, 7 * len(archivos_csv)))
    # Ajustar el espacio vertical entre subgráficos
    plt.subplots_adjust(hspace=0.6)

    # Calculo para cada archivo y ploteo:
    for i, archivo_csv in enumerate(archivos_csv):
        path = os.path.join(DIRECTORIO_ARCHIVOS, archivo_csv)
        tiempos = cargar_tiempos(path)

        print("Archivo {} cargado correctamente con n={}".format(archivo_csv, len(tiempos)))
        nombres_gr = []
        tiempos_gr = []

        for nombre, algoritmo in ALGORITMOS.items():
            t_i = time.time()
            tiempos_ordenados = algoritmo(tiempos.copy())
            resultado_analisis = calcular_tiempo_analisis(tiempos_ordenados)
            t_f = time.time()
            tiempo_ejecucion = t_f - t_i

            nombres_gr.append(nombre)
            tiempos_gr.append(tiempo_ejecucion)

            print("Tiempo final del análisis para {} con {}: {}".format(archivo_csv, nombre, resultado_analisis))

        # Cargo grafico de barras
        bars = axs[i].bar(eje_x + i, tiempos_gr, width=bar_width, label=nombres_gr, color=colores)

        # Encontrar la barra con el menor valor
        min_bar = min(bars, key=lambda bar: bar.get_height())

        # Obtener la altura del rectángulo desde la base hasta la altura máxima de la barra
        rect_height = min_bar.get_height() - axs[i].get_ylim()[0]

        # Remarco el rectangulo con el menor valor.
        rect = plt.Rectangle((min_bar.get_x(), axs[i].get_ylim()[0]), min_bar.get_width(), rect_height, linewidth=3, edgecolor='y', facecolor='none')
        axs[i].add_patch(rect)

        # Agrego sobre cada barra su valor.
        for index, value in enumerate(tiempos_gr):
            axs[i].text(eje_x[index] + i, value, f'{value:.0f}', ha='center', va='bottom')

        axs[i].set_xlabel('Algoritmos', fontsize=10, weight='bold')
        axs[i].set_ylabel('Tiempo de Análisis', fontsize=10, weight='bold')

        # Customizo el eje y para setear limites y desactivar notacion cientifica
        axs[i].set_ylim(bottom=0, top=max(tiempos_gr) * 1.2)
        axs[i].ticklabel_format(axis='y', style='plain')

        axs[i].set_xticks(eje_x + i)
        axs[i].set_xticklabels(nombre_algoritmos)
        # Ajusto la posición de la leyenda
        axs[i].legend(bbox_to_anchor=(1.10, 0.5), loc='center right')
        axs[i].set_title('Comparación de Tiempo de Análisis para {}'.format(archivo_csv))
        axs[i].grid(True)

    plt.savefig('time_execution_comparison_plot.png')
    plt.show()
