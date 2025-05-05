    # ¿Qué imprime el siguiente código?

    # def suma(lista):  
    #     total = 0  
    #     for num in lista:  
    #         total += num  
    #     return total
    # print(suma([1, 2, 3]))

    # a) 6
    # b) [1, 2, 3]
    # c) 123
    # d) Error

    # ¿Qué hace este fragmento de código?

   
    # lista = [3, 1, 4, 1, 5]  
    # print(lista[::-1])
    # a) Imprime la lista sin el primer elemento
    # b) Imprime la lista invertida
    # c) Imprime solo los números pares
    # d) Error

    # ¿Qué estructura es ideal para representar pares clave-valor?
    # a) Lista
    # b) Conjunto
    # c) Diccionario
    # d) Tupla

    # Completa la función para encontrar el mayor número en una lista:

    # python
    # Copiar
    # Editar
    # def maximo(lista):  
    #     max = lista[0]  
    #     for num in lista:  
    #         if _______:  
    #             max = num  
    #     return max
    # ¿Qué va en el espacio en blanco?
    # a) num = max
    # b) num < max
    # c) num > max
    # d) num == max

    # ¿Qué se imprime?

    # python
    # Copiar
    # Editar
    # for i in range(1, 5):  
    #     if i % 2 == 0:  
    #         continue  
    #     print(i)
    # a) 2 4
    # b) 1 2 3 4
    # c) 1 3
    # d) 1 2 3

    # Verdadero o Falso: return detiene la ejecución de una función.

    # ¿Qué resultado da este código?

    # python
    # Copiar
    # Editar
    # x = [1, 2, 3]  
    # y = x  
    # y.append(4)  
    # print(x)
    # a) [1, 2, 3]
    # b) [1, 2, 3, 4]
    # c) [4]
    # d) Error

    # ¿Cuál es la salida del siguiente código?

    # python
    # Copiar
    # Editar
    # def recursivo(n):  
    #     if n == 0:  
    #         return 0  
    #     return n + recursivo(n-1)

    # print(recursivo(3))
    # a) 3
    # b) 6
    # c) Error
    # d) 0

    # ¿Qué valor imprime?

    # python
    # Copiar
    # Editar
    # x = [1, 2, 3]  
    # print(x.pop())
    # a) 1
    # b) 3
    # c) [1, 2]
    # d) Error

    # ¿Para qué sirve la palabra clave elif?
    # a) Finalizar una función
    # b) Declarar otra función
    # c) Evaluar una condición alternativa
    # d) Nada


respuestas = {
    "¿Qué imprime el siguiente código?": "6",
    "¿Qué hace este fragmento de código?": "Imprime la lista invertida",
    "¿Qué estructura es ideal para representar pares clave-valor?": "Diccionario",
    "¿Qué va en el espacio en blanco?": "num > max",
    "¿Qué se imprime?": "1 3",
    "Verdadero o Falso: return detiene la ejecución de una función.": "Verdadero",
    "¿Qué resultado da este código?": "[1, 2, 3, 4]",
    "¿Cuál es la salida del siguiente código?": "6",
    "¿Qué valor imprime?": "3",
    "¿Para qué sirve la palabra clave elif?": "Evaluar una condición alternativa"
}


lista_preguntas_inter = []
for i in respuestas.items():
    lista_preguntas_inter.append({"preguntas":i[0], "respuestas":i[1]})

print(lista_preguntas_inter)
[{'preguntas': '¿Qué imprime el siguiente código?', 'respuestas': '6'}, 
 {'preguntas': '¿Qué hace este fragmento de código?', 'respuestas': 'Imprime la lista invertida'}, 
 {'preguntas': '¿Qué estructura es ideal para representar pares clave-valor?', 'respuestas': 'Diccionario'},
{'preguntas': '¿Qué va en el espacio en blanco?', 'respuestas': 'num > max'},
{'preguntas': '¿Qué se imprime?', 'respuestas': '1 3'}, 
{'preguntas': 'Verdadero o Falso: return detiene la ejecución de una función.', 'respuestas': 'Verdadero'},
 {'preguntas': '¿Qué resultado da este código?', 'respuestas': '[1, 2, 3, 4]'}, 
 {'preguntas': '¿Cuál es la salida del siguiente código?', 'respuestas': '6'}, 
 {'preguntas': '¿Qué valor imprime?', 'respuestas': '3'},
{'preguntas': '¿Para qué sirve la palabra clave elif?', 'respuestas': 'Evaluar una condición alternativa'}]