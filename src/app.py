from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)
    

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    
    
 
    if "label" in request_body and "done" in request_body:
        todos.append(request_body)  
        return jsonify(todos), 200  
    else:
        return jsonify({"error": "Invalid input"}), 400 

@app.route('/todos/<int:position>', methods=['DELETE'])
# def delete_todo(position): 
#     print("This is the position to delete:", position)
#     return 'something'
# def delete_todo(position):
#     if position < 0 or position >= len(todos):
#         return jsonify({"error": "Position out of range"}), 400

def delete_todo(position):
    todos.pop(position)  
    return jsonify(todos)
    
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": True }
]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
