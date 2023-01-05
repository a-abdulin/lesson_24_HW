import os

from flask import Flask, request, jsonify
from marshmallow import ValidationError

from schemas import RequestJsonSchema
from utils import get_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=['POST'])
def post():
    try:
        data = RequestJsonSchema().load(request.json)
    except ValidationError:
        return f'Request is incorrect', 500

    values_cmd = ['sort', 'filter', 'limit', 'map', 'unique', 'regex']
    try:
        if data['cmd1'] not in values_cmd or data['cmd2'] not in values_cmd:
            raise ValidationError
    except ValidationError:
        return f'cmd functions are not correct', 500

    with open(os.path.join(DATA_DIR, data['file_name'])) as result:
        result = get_query(data['cmd1'], data['value1'], result)
        result = get_query(data['cmd2'], data['value2'], result)

    return jsonify(result), 200



if __name__ == '__main__':
    app.run(port=8080)


