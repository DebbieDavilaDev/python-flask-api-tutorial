from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [ { "label": "My first task", "done": False }, { "label": "My second task", "done": False }, { "label": "My third task", "done": False }, { "label": "My fourth task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:indx>', methods=['PUT'])
def update_new_todo(indx):
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos) 

@app.route('/todos/<int:indx>', methods=['DELETE'])
def delete_todo(indx):
    pop_result = todos.pop(indx)
    return jsonify(todos)









if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)