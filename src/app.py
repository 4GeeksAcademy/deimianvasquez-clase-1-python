from flask import Flask


# se crea instancia de flask
app = Flask(__name__)

todos = [
    {
        "id":1,
        "label":"HOla",
        "done":False
    },
     {
        "id":2,
        "label":"Cableada",
        "done":False
    },
     {
        "id":3,
        "label":"Cableada",
        "done":False
    }
]


@app.route('/', methods=["GET"])
def deimian():
    return "Hola ¿qué tal? cómo estas"


@app.route('/todos', methods=["GET"])
def get_todos():
    return todos



if __name__ == '__main__':
    app.run(host='0.0.0.0', port="3001", debug=True)