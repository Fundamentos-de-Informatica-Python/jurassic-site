from flask import Flask,jsonify,request

from src.db.db_manager import load_dinos, save_dinos


app = Flask(__name__)

@app.get('/api/jurassic/hello')
def get_dinos():
    return 'Hello Dinos!'


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
