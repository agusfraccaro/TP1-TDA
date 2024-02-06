import csv
from algoritmo_resolucion import pd_entrenamientos, pd_reconstruccion
from main import cargar_datos

def efectividad(nombre_archivo):
    EI, SI = cargar_datos("casos/efectividad/"+nombre_archivo+".csv")
    matriz = pd_entrenamientos(SI, EI)
    solucion = pd_reconstruccion(matriz)

    with open('casos/efectividad/resoluciones/'+nombre_archivo+"_resol.txt", 'r') as file:
        content = file.read().split(',')
        esperado = [int(value) for value in content]
    #aca chequear que coincida con el resultado esperado
    if(solucion == esperado):
        return True

def main():
    #Lista de nombres de archivos
    archivos = ["2_elem","2_elem_v2","3_elem","5_elem", "5_elem_v2", "10_elem", "15_elem"]
    resultados = []
    for archivo in archivos:
        resultados.append(efectividad(archivo))

    porcentaje_efectividad = (resultados.count(True) / len(resultados)) * 100
    print("\nPorcentaje de efectividad: "+str(porcentaje_efectividad)+"%")

main()