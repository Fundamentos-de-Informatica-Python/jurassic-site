from flask import Flask,jsonify,request
from flask_cors import CORS

from db.db_manager import load_dinos, save_dinos

app = Flask(__name__)
CORS(app)

@app.get('/api/jurassic/hello')
def get_hello():
    return 'Hello Dinos! Do you meet Patagotitan.... Otro Argentino en New York??'

@app.get('/api/jurassic/dinos')
def get_dinos():
    lista_dinos = load_dinos()
    return jsonify([objDino.serialize() for objDino in lista_dinos])


@app.post('/api/jurassic/dinos')
def post_dinos():
    data = request.get_json()

    save_dinos(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
