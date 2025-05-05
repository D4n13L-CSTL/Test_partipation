# ¿Cuál es la complejidad temporal del siguiente algoritmo?

# python
# Copiar
# Editar
# for i in range(n):  
#     for j in range(n):  
#         print(i, j)
# a) O(n)
# b) O(log n)
# c) O(n^2)
# d) O(n!)

# ¿Qué estructura sigue el principio FIFO?
# a) Pila
# b) Cola
# c) Árbol
# d) Lista

# ¿Qué devuelve esta función recursiva?

# python
# Copiar
# Editar
# def f(n):  
#     if n == 1:  
#         return 1  
#     return n * f(n - 1)

# print(f(4))
# a) 4
# b) 10
# c) 24
# d) Error

# ¿Cuál algoritmo de ordenamiento es más eficiente en promedio?
# a) Bubble Sort
# b) Insertion Sort
# c) Merge Sort
# d) Selection Sort

# ¿Qué estructura es más adecuada para realizar una búsqueda binaria?
# a) Lista desordenada
# b) Lista ordenada
# c) Diccionario
# d) Tupla

# ¿Qué hace el siguiente código?


# stack = []  
# stack.append(1)  
# stack.append(2)  
# stack.pop()  
# print(stack)
# a) [1, 2]
# b) [1]
# c) []
# d) [2]

# ¿Cuál sería una buena forma de representar un grafo no dirigido en código?
# a) Lista simple
# b) Diccionario de listas
# c) Lista de enteros
# d) Tupla

# ¿Cuál es la salida?

# python
# Copiar
# Editar
# def quicksort(arr):  
#     if len(arr) <= 1:  
#         return arr  
#     pivot = arr[0]  
#     menores = [x for x in arr[1:] if x <= pivot]  
#     mayores = [x for x in arr[1:] if x > pivot]  
#     return quicksort(menores) + [pivot] + quicksort(mayores)

# print(quicksort([3, 2, 1]))
# a) [1, 2, 3]
# b) [3, 2, 1]
# c) Error
# d) [2, 3, 1]

# ¿Cuál es la salida?

# x = {'a': 1, 'b': 2}  
# print(x.get('c', 3))
# a) 3
# b) 'c'
# c) None
# d) Error

# ¿Cuál NO es una característica de la recursión?
# a) Llamada a sí misma
# b) Base case
# c) Stack overflow posible
# d) Uso de while explícito

respuestas_correctas = {
    "¿Cuál es la complejidad temporal del siguiente algoritmo?": "O(n^2)",
    "¿Qué estructura sigue el principio FIFO?": "Cola",
    "¿Qué devuelve esta función recursiva?": "24",
    "¿Cuál algoritmo de ordenamiento es más eficiente en promedio?": "Merge Sort",
    "¿Qué estructura es más adecuada para realizar una búsqueda binaria?": "Lista ordenada",
    "¿Qué hace el siguiente código?": "[1]",
    "¿Cuál sería una buena forma de representar un grafo no dirigido en código?": "Diccionario de listas",
    "¿Cuál es la salida? (quicksort)": "[1, 2, 3]",
    "¿Cuál es la salida? (diccionario con get)": "3",
    "¿Cuál NO es una característica de la recursión?": "Uso de while explícito"
}

lista_preguntas_avanzado = []
for i in respuestas_correctas.items():
    lista_preguntas_avanzado.append({"preguntas":i[0], "respuestas":i[1]})
print(lista_preguntas_avanzado)



[{'preguntas': '¿Cuál es la complejidad temporal del siguiente algoritmo?', 'respuestas': 'O(n^2)'}, 
 {'preguntas': '¿Qué estructura sigue el principio FIFO?', 'respuestas': 'Cola'}, 
 {'preguntas': '¿Qué devuelve esta función recursiva?', 'respuestas': '24'}, 
 {'preguntas': '¿Cuál algoritmo de ordenamiento es más eficiente en promedio?', 'respuestas': 'Merge Sort'},
 {'preguntas': '¿Qué estructura es más adecuada para realizar una búsqueda binaria?', 'respuestas': 'Lista ordenada'},
{'preguntas': '¿Qué hace el siguiente código?', 'respuestas': '[1]'},
 {'preguntas': '¿Cuál sería una buena forma de representar un grafo no dirigido en código?', 'respuestas': 'Diccionario de listas'}, 
 {'preguntas': '¿Cuál es la salida? (quicksort)', 'respuestas': '[1, 2, 3]'},
   {'preguntas': '¿Cuál es la salida? (diccionario con get)', 'respuestas': '3'},
     {'preguntas': '¿Cuál NO es una característica de la recursión?', 'respuestas': 'Uso de while explícito'}]