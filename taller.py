from random import randint


def countOneOne(lanzamientos):
    contador = 0
    for dado1, dado2 in lanzamientos:
        if dado1 == 1 and dado2 == 1:
            contador += 1
    return contador


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return [dado1, dado2]



N = 1000000
lanzamientos = []
for i in range(N):
    lanzamientos.append(lanzar_dados())


contador = countOneOne(lanzamientos)
print(f"Número de veces que se obtuvieron dos unos: {contador}")

#Análisis funcionamiento del programa 
#Lanzar_dados genera dos números aleatorios entre 1 y 6, simulando el lanzamiento de dos dados. Y los retorna dentro de una lista [dado1, dado2].
#ciclo for ejecuta lanzar_dados N veces (1,000,000 en este caso) y almacena los resultados en la lista lanzamientos.
#counteOneOne recibe la lista de lanzamientos y cuenta cuántas veces ambos dados muestran un 1, incrementando el contador cada vez que se cumple esta condición.
