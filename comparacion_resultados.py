from typing import List, Dict

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

from algoritmos import ALGORITMOS, calcular_tiempo_analisis_completo
from casos.generacion_casos import generar_tamanios_comparacion, generar_casos, generar_tamanios_potencias, \
    generar_tamanios_grande


def graficar_comparacion_tiempos(casos: List[List[int]]) -> None:

    nombre_algoritmos = list(ALGORITMOS.keys())
    colores = ['tab:blue', 'tab:orange', 'tab:green']
    eje_x = np.arange(len(nombre_algoritmos))
    bar_width = 0.3
    cant_columnas = 2

    fig, (axs) = plt.subplots(len(casos) // cant_columnas, cant_columnas, figsize=(35, 25))
    plt.subplots_adjust(hspace=0.3, wspace=0.3)

    # Calculo los dias para cada caso y ploteo
    for i, caso in enumerate(casos):
        nombres_gr = []
        tiempos_gr = []

        for nombre, algoritmo in ALGORITMOS.items():
            dias_de_analisis = calcular_tiempo_analisis_completo(caso.copy(), algoritmo)

            nombres_gr.append(nombre)
            tiempos_gr.append(dias_de_analisis)

        ax = axs[i // cant_columnas][i % cant_columnas]
        bars = ax.bar(eje_x + i, tiempos_gr, width=bar_width, label=nombres_gr, color=colores)

        # Remarco las barras con menor valor
        first_min_bar = min(bars, key=lambda bar: bar.get_height())
        min_bars = [bar for bar in bars if bar.get_height() == first_min_bar.get_height()]

        rect_height = first_min_bar.get_height() - ax.get_ylim()[0]
        for bar in min_bars:
            rect = plt.Rectangle((bar.get_x(), ax.get_ylim()[0]), bar.get_width(), rect_height, linewidth=3, edgecolor='r', facecolor='none')
            ax.add_patch(rect)

        # Agrego sobre cada barra su valor.
        for index, value in enumerate(tiempos_gr):
            ax.text(eje_x[index] + i, value, f'{value:.0f}', ha='center', va='bottom', fontsize=20)

        ax.set_title(f'Comparación de tiempo de análisis para {len(caso)} rivales', fontsize=30)
        ax.set_xlabel('Algoritmo utilizado', fontsize=20, weight='bold')
        ax.set_ylabel('Tiempo de análisis (días)', fontsize=20, weight='bold')

        # Establezco limites en el eje y
        ax.tick_params(axis='y', labelsize=20)
        ax.tick_params(axis='x', labelsize=20)
        ax.set_ylim(bottom=0, top=max(tiempos_gr) * 1.4)
        ax.ticklabel_format(axis='y', style='plain')

        ax.set_xticks(eje_x + i)
        ax.set_xticklabels(nombre_algoritmos)

        # Ajusto la leyenda
        legend_handles = [Rectangle((0, 0), 0, 0, color=color, label=label) for color, label in zip(colores, nombres_gr)]
        legend_handles.append(Line2D([0], [0], color='r', label="Resultado mínimo"))
        ax.legend(loc='upper right', handles=legend_handles, fontsize=15)

    plt.savefig('graficos/results_comparison_plot.png')


def calcular_efectividad_global(casos: List[List[int]], algoritmos: Dict[str, callable]) -> Dict[str, float]:
    efectividad_global = {nombre: 0.0 for nombre in algoritmos.keys()}

    for caso in casos:
        tiempos_algoritmos = {
            nombre: calcular_tiempo_analisis_completo(caso.copy(), algoritmo)
            for nombre, algoritmo in algoritmos.items()
        }

        mejores_algoritmos = [
            algoritmo for algoritmo, tiempo in tiempos_algoritmos.items()
            if tiempo == min(tiempos_algoritmos.values())
        ]

        print(tiempos_algoritmos)
        for nombre in mejores_algoritmos:
            efectividad_global[nombre] += 1.0

    total_casos = len(casos)
    efectividad_global = {
        nombre: (efectividad / total_casos) * 100.0
        for nombre, efectividad in efectividad_global.items()
    }

    return efectividad_global


def graficar_efectividad(efectividad: Dict[str, float], nombre_plot) -> None:
    nombres_algoritmos = list(efectividad.keys())
    porcentajes_efectividad = list(efectividad.values())
    colores = ['tab:blue', 'tab:orange', 'tab:green']

    plt.figure(figsize=(10, 6))
    bars = plt.bar(nombres_algoritmos, porcentajes_efectividad, color=colores)

    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.5,
            f'{bar.get_height():.2f}%',
            ha='center',
            va='bottom',
            fontsize=12
        )

    plt.xlabel('Algoritmo utilizado', fontsize=14, weight='bold')
    plt.ylabel('Porcentaje de efectividad', fontsize=14, weight='bold')
    plt.title('Porcentaje de efectividad de cada algoritmo', fontsize=16, weight='bold')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.ylim(0, 110)

    plt.savefig(f'graficos/{nombre_plot}.png')


def analizar_resultados_tiempo_analisis() -> None:
    tamanios = generar_tamanios_comparacion()
    print(f"Comparando resultados con los siguientes tamaños: {tamanios}")
    casos = generar_casos(tamanios)
    graficar_comparacion_tiempos(casos)

def analizar_resultados_efectividad_potencias() -> None:
    tamanios = generar_tamanios_potencias()
    print(f"Comparando efectividad con los siguientes tamaños: {tamanios}")
    casos = generar_casos(tamanios)
    efectividad_global = calcular_efectividad_global(casos, ALGORITMOS)
    graficar_efectividad(efectividad_global, "efectivity_powers_two")


def analizar_resultados_efectividad_expandido() -> None:
    tamanios = generar_tamanios_grande()
    print(f"Comparando efectividad con los siguientes tamaños: {tamanios}")
    casos = generar_casos(tamanios)
    efectividad_global = calcular_efectividad_global(casos, ALGORITMOS)
    graficar_efectividad(efectividad_global, "efectivity_expanded")

def main():
    analizar_resultados_tiempo_analisis()
    analizar_resultados_efectividad_expandido()
    analizar_resultados_efectividad_potencias()


main()
