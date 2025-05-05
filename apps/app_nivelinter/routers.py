from flask import Blueprint, render_template, request,redirect,url_for,jsonify, session,flash

app_intermedio = Blueprint('intermedio', __name__)


preguntas_respuestas = [{'preguntas': '¿Qué imprime el siguiente código?', 'respuestas': '6'}, 
 {'preguntas': '¿Qué hace este fragmento de código?', 'respuestas': 'Imprime la lista invertida'}, 
 {'preguntas': '¿Qué estructura es ideal para representar pares clave-valor?', 'respuestas': 'Diccionario'},
{'preguntas': '¿Qué va en el espacio en blanco?', 'respuestas': 'num > max'},
{'preguntas': '¿Qué se imprime?', 'respuestas': '1 3'}, 
{'preguntas': 'Verdadero o Falso: return detiene la ejecución de una función.', 'respuestas': 'True'},
 {'preguntas': '¿Qué resultado da este código?', 'respuestas': '[1, 2, 3, 4]'}, 
 {'preguntas': '¿Cuál es la salida del siguiente código?', 'respuestas': '55'}, 
 {'preguntas': '¿Qué valor imprime?', 'respuestas': '3'},
{'preguntas': '¿Para qué sirve la palabra clave elif?', 'respuestas': 'Evaluar una condición alternativa'}]




@app_intermedio.route("/api/verificar", methods=["POST"])
def verificar_inter():
    data = request.json  
    
    resultados = []
    for item in data:
        index = item.get("index")
        respuesta = item.get("respuesta")
        
        if index < len(preguntas_respuestas):
            correcta = preguntas_respuestas[index]["respuestas"]
            es_correcto = str(respuesta).strip().lower() == str(correcta).strip().lower()
            resultados.append({
                "index": index,
                "pregunta": preguntas_respuestas[index]["preguntas"],
                "respuesta_usuario": respuesta,
                "correcto": es_correcto
            })
        else:
            resultados.append({
                "index": index,
                "error": "Índice fuera de rango"
            })
    
    return jsonify(resultados)