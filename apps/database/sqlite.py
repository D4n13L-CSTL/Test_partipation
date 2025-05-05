import sqlite3


def insertar_user(*args):
    conexion = sqlite3.connect('registros.db')
    curson = conexion.cursor()
    curson.execute("INSERT INTO users (nombre, basico, intermedio,avanzado, correctas_basica,incorrectas_basicas, correctas_intermedias, incorrectas_intermedias, correctas_avanced, incorrectas_avanced) VALUES(?,?,?,?,?,?,?,?,?,?)", args)
    conexion.commit()
    conexion.close()


def consulta_codigo_tio():
    conexion = sqlite3.connect('registros.db')
    curson = conexion.cursor()
    curson.execute('SELECT * FROM users')
    data = curson.fetchall()
    conexion.close()
    return data






