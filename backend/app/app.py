import flask
from flask import Flask
from flask_cors import CORS, cross_origin
from flask import request, jsonify
import json
import os
import torch

import segmentation

UPLOAD_FOLDER = './files/'

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
    os.mkdir(f'{UPLOAD_FOLDER}/images')
elif not os.path.exists(f'{UPLOAD_FOLDER}/images'):
    os.mkdir(f'{UPLOAD_FOLDER}/images')

model = torch.hub.load('/home/tiveron/faculdade/AM/a/trabalho-final-am/backend/yolov5', 'custom', path='./best.pt', source='local')

print('UUUUUUUUAAAAAAAAAAAAAAAAHHHHHHHHHHH')

@app.route('/', methods=['POST'])
@cross_origin(origin='*',headers=['Content-Type'])
def hello():
    if 'file' in request.files:
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        resposta = segmentation.faz_tudo(file.filename, model)
        os.remove('./files/'+ file.filename)



    return jsonify(resposta)

if __name__ == '__main__':
    app.run()
