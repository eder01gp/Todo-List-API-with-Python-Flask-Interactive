from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first tasks", "done": False },
    { "label": "My second tasks", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    json_text = jsonify(todos)
    return json_text, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    filter(lambda e: todos.index(e)==position, todos)
    json_text = jsonify(todos)
    return json_text, 200









if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)