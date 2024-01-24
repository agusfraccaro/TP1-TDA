# Teoria de Algoritmos - Buchwald

Trabajo Práctico 1: Algoritmos Greedy

## Integrantes
* Emanuel Pelozo 99444
* Agustina Fraccaro 103199
* Agustina Schmidt 103409
* Matias Gonzalez 104913

## Dependencias

* Python >= 3.10
* pip >= 22.0

## Instalación

```bash
make deps
```

## Ejecución

```bash
python3 main.py -p <path> -a <algoritmo>
```

Algoritmos posibles:

* `ayudante`: Ordena por A_i en orden descendiente (default y optimo)
* `diferencia`: Ordena por A_i - S_i en orden descendiente
* `scaloni`: Ordena por S_i en orden ascendente

Para mas info sobre parametros:

```bash
python3 main.py -h
```