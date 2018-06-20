# coding=utf-8
# !/usr/bin/env python

'''
--------------------------------------------------------------------------------
Descripción general:
Este archivo define el rol del API Gateway. Su función general es ser el
intermediario entre el cliente y los microservicios para que de esta manera
la comunicación sea únicamente entre estas dos entidades y aquí se gestionen
los aspectos pertinentes al consumo de APIs.
--------------------------------------------------------------------------------
Descripción de los elementos:
- API Gateway
    Responsabilidad
        - Ofrecer una interfaz para la comunicación con los diferentes
        microservicios del sistema.
    Propiedades:
        - Se comunica con los microservicios suma, resta, multiplicacion y division.
        - Proporciona al cliente una interfaz para la comunicación por medio
        de una API.
'''

import os
import requests
from flask import request, render_template
from flask.ext.api import FlaskAPI


'''
--------------------------------------------------------------------------------
Definición del API Gateway
--------------------------------------------------------------------------------
'''
app = FlaskAPI(__name__)

# servicio de suma.py
@app.route("/api/suma", methods=['GET'])
def suma():
    url = 'http://localhost:8081/suma'
    response = requests.get(url, request.args)
    return response.json(), response.status_code

# servicio de resta de nodjs
@app.route("/api/resta", methods=['GET'])
def resta():
    url = 'http://localhost:8000/resta'
    response = requests.get(url, request.args)
    return response.json(), response.status_code

# servicios de multiplicacion spring boot java
@app.route("/api/multiplicacion", methods=['GET'])
def multiplicacion():
    url = 'http://localhost:8080/multiplicar'
    response =requests.get(url,request.args)
    return response.json(),response.status_code

# servicios de division de laravel php
@app.route("/api/division", methods=['GET'])
def division():
    url = 'http://127.0.0.1:8090/division'
    n1 = request.args['n1']
    n2 = request.args['n2']
    print n1+'  '+n2
    response =requests.get(url+'/'+n1+'/'+n2)
    return response.json(),response.status_code


'''
--------------------------------------------------------------------------------
Ejecución del API Gateway
--------------------------------------------------------------------------------
'''

if __name__ == '__main__':
    print '--------------------------------------------------------------------'
    print 'API Gateway'
    print '--------------------------------------------------------------------'
    port = int(os.environ.get('PORT', 8085))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
