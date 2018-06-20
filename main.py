# coding=utf-8
# !/usr/bin/env python

'''
Descripción general:
Este script levanta los servicios y demás elementos necesarios para el
funcionamiento del sistema.
--------------------------------------------------------------------------------
'''

import os
import webbrowser


# Métodos que levantan los servicios en una nueva terminal.
def run_python_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"python " + program_name + "\"'")

def run_node_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"node " + program_name + "\"'")

def run_java_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"java -jar " + program_name + "\"'")

def run_php_program(program_name):
    os.system("gnome-terminal -e 'bash -c \"php " + program_name + " serve --port 8090\"'")

print 'Levantando el microservicio servicios suma'
run_python_program('servicios/suma.py')

print 'Levantando el microservicio servicios resta'
run_node_program('servicios/api/resta.js')

print 'Levantando el servicio java multiplicacion'
run_java_program('servicios/microservicios-0.0.1-SNAPSHOT.jar')

print 'Levantando el servicio php laravel division'
run_php_program('servicios/laravel/artisan')


# Se levanta el API Gateway.
print 'Levantando el api_gateway.py'
run_python_program('api_gateway.py')


# Se levanta la GUI.
print 'Levantando el gui.py'
run_python_program('gui.py')

# Se acabó la inicialización del sistema
# print 'Los componentes necesarios fueron levantados'

webbrowser.open('http://localhost:8088', new=0)
