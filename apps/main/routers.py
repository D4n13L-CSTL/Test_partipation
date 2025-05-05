from flask import Blueprint, render_template, request,redirect,url_for,jsonify, session,flash
app_main = Blueprint('app_main', __name__)




preguntas_respuestas = [
    {"pregunta": "¿Cuál es el resultado de la siguiente expresión: 3 + 4 * 2?", "respuesta": "11"},
    {"pregunta": "¿Qué estructura permite repetir un bloque de código mientras se cumpla una condición?", "respuesta": "while"},
    {"pregunta": "¿Cuál es el tipo de dato de True en la mayoría de lenguajes?", "respuesta": "bool"},
    {"pregunta": "¿Cuál es la salida del siguiente código?", "respuesta": "False"},
    {"pregunta": "¿Qué hace un condicional if?", "respuesta": "Evalúa condiciones y ejecuta código según el resultado"},
    {"pregunta": "Verdadero o Falso: El siguiente código es válido.", "respuesta": "True"},
    {"pregunta": "¿Cuál de las siguientes estructuras permite almacenar múltiples valores en orden?", "respuesta": "list"},
    {"pregunta": "¿Qué devuelve len([1, 2, 3, 4])?", "respuesta": "4"},
    {"pregunta": "¿Cuál es la forma correcta de definir una función en Python?", "respuesta":"def funcion():"},
    {"pregunta": "¿Cuál de los operadores se usa para comparar igualdad?", "respuesta": "=="}
]


repuesta_if = [
   "Evalúa condiciones y ejecuta código según el resultado",
   "declara variables",
   "ejecuta funciones"
]

respuetas7 = ["int","list","bool","float"]

respuesta9 = ["funcion() {}","def funcion():","function funcion()" , "define funcion()"]






@app_main.route("/")
def render():
   preguntas  = [i['pregunta'] for i in preguntas_respuestas]
   return render_template('main.html' , preguntas = preguntas, repuesta_if = repuesta_if, respuetas7 = respuetas7, respuesta9 = respuesta9)
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

preguntas_intermedias = [
    "¿Qué imprime el siguiente código?",
    "¿Qué hace este fragmento de código?",
    "¿Qué estructura es ideal para representar pares clave-valor?",
    "Completa la función para encontrar el mayor número en una lista: ¿Qué va en el espacio en blanco?",
    "¿Qué se imprime?",
    "Verdadero o Falso: return detiene la ejecución de una función.",
    "¿Qué resultado da este código?",
    "¿Cuál es la salida del siguiente código?",
    "¿Qué valor imprime?",
    "¿Para qué sirve la palabra clave elif?"
]

respuestas1 = ["6","[1, 2, 3]","123", "Error"]

opciones2 = ["Imprime la lista sin el primer elemento","Imprime la lista invertida","Imprime solo los números pares","Error"]

opciones3 = [ "Lista","Conjunto","Diccionario","Tupla"]

opciones_4_inter = [
    "num = max",
    "num < max",
    "num > max",
    "num == max"
]

opciones_5_inter = [
    "2 4",
    "1 2 3 4",
    "1 3",
    "1 2 3"
]

opciones_6_inter = [
    "True",
    "False"
]

opciones_7_inter = [
    "[1, 2, 3]",
    "[1, 2, 3, 4]",
    "[4]",
    "Error"
]

opciones_8_inter = [
    "3",
    "55",
    "10",
    "Error",
    "9"
]

opciones_9_inter = [
    "1",
    "3",
    "[1, 2]",
    "Error"
]

opciones_10_inter = [
    "Finalizar una función",
    "Declarar otra función",
    "Evaluar una condición alternativa",
    "Nada"
]



@app_main.route("/inter")
def render_inter():
   return render_template("inter.html", ask = preguntas_intermedias, respuestas1 = respuestas1, opciones2 =opciones2 , opciones3 = opciones3,
                          opciones_4 = opciones_4_inter, 
                          opciones_5 = opciones_5_inter, 
                          opciones_6 = opciones_6_inter, 
                          opciones_7 = opciones_7_inter, 
                          opciones_8 = opciones_8_inter, 
                          opciones_9 = opciones_9_inter, 
                          opciones_10 = opciones_10_inter, 
                        
                          )












preguntas_avanzadas = [
    "¿Cuál es la complejidad temporal del siguiente algoritmo?",
    "¿Qué estructura sigue el principio FIFO?",
    "¿Qué devuelve esta función recursiva?",
    "¿Cuál algoritmo de ordenamiento es más eficiente en promedio?",
    "¿Qué estructura es más adecuada para realizar una búsqueda binaria?",
    "¿Qué hace el siguiente código?",
    "¿Cuál sería una buena forma de representar un grafo no dirigido en código?",
    "¿Cuál es la salida de este codigo?",
    "¿Cuál es la salida?",
    "¿Cuál NO es una característica de la recursión?"
]


opciones_1 = ["O(n)", "O(log n)", "O(n^2)", "O(n!)"]
opciones_2 = ["Pila", "Cola ", "Árbol", "Lista"]
opciones_3 = ["4", "10", "24", "Error"]
opciones_4 = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Selection Sort"]
opciones_5 = ["Lista desordenada", "Lista ordenada", "Diccionario", "Tupla"]
opciones_6 = ["[1, 2]", "[1]", "[]", "[2]"]
opciones_7 = ["Lista simple", "Diccionario de listas", "Lista de enteros", "Tupla"]
opciones_8 = ["[1, 2, 3]", "[3, 2, 1]", "Error", "[2, 3, 1]"]
opciones_9 = ["3", "'c'", "None", "Error"]
opciones_10 = ["Llamada a sí misma", "Base case", "Stack overflow posible", "Uso de while explícito"]


@app_main.route("/avanzado")
def render_avanzado():
   return render_template("avanzado.html", preguntas_avanzadas = preguntas_avanzadas,
                          opciones_1 = opciones_1,
                          opciones_2 = opciones_2,
                          opciones_3 = opciones_3,
                          opciones_4 = opciones_4,
                          opciones_5 = opciones_5,
                          opciones_6 = opciones_6,
                          opciones_7 = opciones_7,
                          opciones_8 = opciones_8,
                          opciones_9 = opciones_9,
                          opciones_10 = opciones_10
                           )