import json
import os
import requests
from flask import request
from flask.ext.api import FlaskAPI, status

app = FlaskAPI(__name__)

@app.route("/suma",methods=['GET'])
def resultado():
        n1 = request.args['n1']
        n2 = request.args['n2']
        s=int(n1)+int(n2)
        resul = {'suma': s}
        return resul

if __name__ == '__main__':
    print 'Servicio suma.py'
    port = int(os.environ.get('PORT', 8081))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
