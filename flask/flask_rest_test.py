#!/usr/bin/env python
# coding=utf-8

#
# ./flask_rest_test.py
# and 
# curl -i http://127.0.0.1:5000/todo/api/v1.0/tasks
#


from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Pyhton',
        'description': u'Need to find',
        'done': False
    }

]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
    app.run(debug=True)
