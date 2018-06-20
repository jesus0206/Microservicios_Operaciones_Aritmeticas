# coding=utf-8
# !/usr/bin/env python

'''
Descripción general:
Este archivo define la interfaz gráfica del usuario. Recibe los parámetros que
posteriormente son enviados al API Gateway para la comunicación con los
servicios que utiliza el sistema.
--------------------------------------------------------------------------------
Descripción de los elementos:
- GUI
    Responsabilidad
        - Proporcionar la interfaz gráfica con la que el usuario hará uso del
        sistema.
    Propiedades:
        - Consume el API Gateway que se comunica con los servicios que
        proporcionan información al usuario.
'''

import os
from flask import Flask, render_template, request
import json
import requests

'''
--------------------------------------------------------------------------------
Definición de las rutas con las que se comunica la GUI.
--------------------------------------------------------------------------------
'''

app = Flask(__name__)


# Ruta que renderiza la pantalla principal del sistema.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/suma", methods=['GET'])
def operacion_sumar():
    # Solicitud al servicio sumar, por medio del API Gateway.
    url = 'http://localhost:8085/api/suma'
    json_result = {'suma': {}, 'resta': {}, 'multiplicacion': {},'division':{}}
    response = requests.get(url, request.args)
    if response.status_code == 200:
        json_result['suma'] = response.json()
        json_result['suma']['display'] = ''
    else:
        json_result['suma']['display'] = 'hidden'
    return render_template("suma.html", result=json_result)

@app.route("/resta", methods=['GET'])
def operacion_resta():
    # Solicitud al servicio sumar, por medio del API Gateway.
    url = 'http://localhost:8085/api/resta'
    response = requests.get(url, request.args)
    json_result = {'suma': {}, 'resta': {}, 'multiplicacion': {},'division':{}}
    if response.status_code == 200:
        json_result['resta'] = response.json()
        json_result['resta']['display'] = ''
    else:
        json_result['resta']['display'] = 'hidden'
    return render_template("resta.html", result=json_result)

@app.route("/multiplicacion", methods=['GET'])
def operacion_multi():
    # Solicitud al servicio sumar, por medio del API Gateway.
    url = 'http://localhost:8085/api/multiplicacion'
    response = requests.get(url, request.args)
    json_result = {'suma': {}, 'resta': {}, 'multiplicacion': {},'division':{}}
    if response.status_code == 200:
        json_result['multiplicacion'] = response.json()
        json_result['multiplicacion']['display'] = ''
    else:
        json_result['multiplicacion']['display'] = 'hidden'
    return render_template("multi.html", result=json_result)


@app.route("/division", methods=['GET'])
def operacion_div():
    # Solicitud al servicio sumar, por medio del API Gateway.
    url = 'http://localhost:8085/api/division'
    response = requests.get(url, request.args)
    json_result = {'suma': {}, 'resta': {}, 'multiplicacion': {},'division':{}}
    if response.status_code == 200:
        json_result['division'] = response.json()
        json_result['division']['display'] = ''
    else:
        json_result['division']['display'] = 'hidden'
    return render_template("division.html", result=json_result)

@app.route("/calcular", methods=['GET'])
def operacion_general():
    # Solicitud al servicio sumar, por medio del API Gateway.
#division 
    json_result = {'suma': {}, 'resta': {}, 'multiplicacion': {},'division':{}}
    url = 'http://localhost:8085/api/division'
    response = requests.get(url, request.args)
    if response.status_code == 200:
        json_result['division'] = response.json()
    else:
        json_result['division']['display'] = 'hidden'
# multiplicacion
    url = 'http://localhost:8085/api/multiplicacion'
    response = requests.get(url, request.args)
    if response.status_code == 200:
        json_result['multiplicacion'] = response.json()
    else:
        json_result['multiplicacion']['display'] = 'hidden'
# resta
    url = 'http://localhost:8085/api/resta'
    response = requests.get(url, request.args)
    if response.status_code == 200:
        json_result['resta'] = response.json()
    else:
        json_result['resta']['display'] = 'hidden'
# suma
    url = 'http://localhost:8085/api/suma'
    response = requests.get(url, request.args)
    if response.status_code == 200:
        json_result['suma'] = response.json()
    else:
        json_result['suma']['display'] = 'hidden'

    return render_template("general.html", result=json_result)



'''
--------------------------------------------------------------------------------
Ejecución del la GUI
--------------------------------------------------------------------------------
'''

if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'GUI'
    print '--------------------------------------------------------------------'
    port = int(os.environ.get('PORT', 8088))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
