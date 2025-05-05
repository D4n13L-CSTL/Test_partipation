from flask import Blueprint, render_template, request,redirect,url_for,jsonify, session,flash

app_avanzado= Blueprint('avanzado', __name__)
preguntas_respuestas = [{'preguntas': '¿Cuál es la complejidad temporal del siguiente algoritmo?', 'respuestas': 'O(n^2)'}, 
 {'preguntas': '¿Qué estructura sigue el principio FIFO?', 'respuestas': 'Cola'}, 
 {'preguntas': '¿Qué devuelve esta función recursiva?', 'respuestas': '24'}, 
 {'preguntas': '¿Cuál algoritmo de ordenamiento es más eficiente en promedio?', 'respuestas': 'Merge Sort'},
 {'preguntas': '¿Qué estructura es más adecuada para realizar una búsqueda binaria?', 'respuestas': 'Lista ordenada'},
{'preguntas': '¿Qué hace el siguiente código?', 'respuestas': '[1]'},
 {'preguntas': '¿Cuál sería una buena forma de representar un grafo no dirigido en código?', 'respuestas': 'Diccionario de listas'}, 
 {'preguntas': '¿Cuál es la salida? (quicksort)', 'respuestas': '[1, 2, 3]'},
   {'preguntas': '¿Cuál es la salida? (diccionario con get)', 'respuestas': '3'},
     {'preguntas': '¿Cuál NO es una característica de la recursión?', 'respuestas': 'Uso de while explícito'}]






@app_avanzado.route("/api/verificar", methods=["POST"])
def verificar_avanzado():
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

@app_avanzado.route("/api/ver", methods=["POST"])
def verificar_avanzadover():
    data = request.json
    index  = data['prueba']
    print(index)