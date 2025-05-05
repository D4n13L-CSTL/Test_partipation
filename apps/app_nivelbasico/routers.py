from flask import Blueprint, render_template, request,redirect,url_for,jsonify, session,flash

app_basico = Blueprint('app_basica', __name__)

preguntas_respuestas = [
    {"pregunta": "¿Cuál es el resultado de la siguiente expresión: 3 + 4 * 2?", "respuesta": "11"},
    {"pregunta": "¿Qué estructura permite repetir un bloque de código mientras se cumpla una condición?", "respuesta": "while"},
    {"pregunta": "¿Cuál es el tipo de dato de True en la mayoría de lenguajes?", "respuesta": "bool"},
    {"pregunta": "¿Cuál es la salida del siguiente código?\n\na = 5\nb = 3\nprint(a > b and b < 2)", "respuesta": "False"},
    {"pregunta": "¿Qué hace un condicional if?", "respuesta": "Evalúa condiciones y ejecuta código según el resultado"},
    {"pregunta": "Verdadero o Falso: El siguiente código es válido.\n\nfor i in range(3):\n    print(i)", "respuesta": "True"},
    {"pregunta": "¿Cuál de las siguientes estructuras permite almacenar múltiples valores en orden?", "respuesta": "list"},
    {"pregunta": "¿Qué devuelve len([1, 2, 3, 4])?", "respuesta": "4"},
    {"pregunta": "¿Cuál es la forma correcta de definir una función en Python?", "respuesta": "def funcion():"},
    {"pregunta": "¿Cuál de los siguientes operadores se usa para comparar igualdad?", "respuesta": "=="}
]


@app_basico.route("/api/verificar", methods=["POST"])
def verificar_todas():
    data = request.json  
    
    resultados = []
    for item in data:
        index = item.get("index")
        respuesta = item.get("respuesta")
        
        if index < len(preguntas_respuestas):
            correcta = preguntas_respuestas[index]["respuesta"]
            es_correcto = str(respuesta).strip().lower() == str(correcta).strip().lower()
            resultados.append({
                "index": index,
                "pregunta": preguntas_respuestas[index]["pregunta"],
                "respuesta_usuario": respuesta,
                "correcto": es_correcto
            })
        else:
            resultados.append({
                "index": index,
                "error": "Índice fuera de rango"
            })
    
    return jsonify(resultados)