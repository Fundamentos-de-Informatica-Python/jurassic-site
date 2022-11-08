from flask import Flask,jsonify,request
from flask_cors import CORS

from db.db_manager import load_dinos, save_dinos

app = Flask(__name__)
CORS(app)




@app.get('/api/jurassic/hello')
def get_dinos():
    return 'Hello Dinos! Do you meet to  Trex??'


@app.get('/api/jurassic/dinos')
def get_hello():
    lista_dinos = load_dinos()
    return jsonify([restr.serialize() for restr in lista_dinos])


@app.route('/api/jurassic/dinos', methods = ['POST'])
def do_post():
    data = request.get_json()

    save_dinos(data)
    return jsonify(data)


if __name__ == '__main__':
    app.run()
