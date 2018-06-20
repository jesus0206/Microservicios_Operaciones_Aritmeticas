# Arquitectura de Microservicios

## Sistema de Operaciones Aritmeticas
En este sistema se realizaran operaciones aritmeticas en diferentes lenguajes de programacion
## Instrucciones para hacer uso de los microservicios
### 1. Comandos para instalar las dependencias de python necesarias para que funcione  la arquitectura
```
sudo pip install Flask==0.10.1  
sudo pip install requests==2.12.4
sudo pip install Flask-API
sudo apt-get install curl
sudo pip install twython
sudo pip install 'requests[security]' 
```

### 2. Descargar el proyecto
```
git clone https://github.com/jesus0206/Microservicios_Operaciones_Aritmeticas.git
```

### 3. Correr el proyecto que levanta los servicio y el navegador para acceder a los servicios
```
si cuenta con SO linux correr archivo
  python main.py que se encarga de levantar los servicios y se abrira un navegador automaticamente
si no cuenta con SO linux correr los servicios de manera independiente  que se encuentra en la carpeta servicios 
para leventar los servicios en diferentes terminales
  
  python servicios/suma.py
  nodee servicios/api/resta.js
  java -jar servicios/microservicios-0.0.1-SNAPSHOT.jar
  php  servicios/laravel/artisan serve --port 8090
  
  python api_gateway.py
  python gui.py
  
  acceder a http://localhost:8088 para probar los microservicios
```
