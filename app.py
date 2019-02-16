
"""import flask

app = flask.Flask(__name__)
@app.route('/')
def index():
    return flask.send_from_directory()

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task)==0:
        flask.abort(404)
    return flask.jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
    return flask.make_response(flask.jsonify({'error': 'Not found'}), 404)

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not flask.request.json or not 'title' in flask.request.json:
        flask.abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': flask.request.json['title'],
        'description': flask.request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return flask.jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)"""