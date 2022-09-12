from flask import Flask,jsonify,request


app = Flask(__name__)

@app.get('/hello')
def get_hello():
    return 'Hello app!'


if __name__ == '__main__':
    app.run(threaded=True, port=5010)
