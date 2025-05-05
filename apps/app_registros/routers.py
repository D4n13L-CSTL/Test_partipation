from flask import Blueprint, render_template, request,redirect,url_for,jsonify, session,flash
from ..database.sqlite import insertar_user

app_registrar = Blueprint("registro", __name__)

@app_registrar.route("/registrar", methods = ['POST'])
def registro():
    try:
        data = request.json
        
        insertar_user(data['user'], data['basico'], data['intermedio'], data['avanzado'], data['correctas'], data['incorrectas'], data['correctas_intermedia'], data['incorrectas_intermedia'], data['correctas_avanced'], data['incorrectas_avanced'] )
        session['user']  = data['user']
        sesiones  = session['user']
        return jsonify (sesiones)
        
    except Exception as e:
        return jsonify({"Error":e}), 500
