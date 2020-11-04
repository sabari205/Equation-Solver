import os
import json
import base64
import shutil
from main import main
from io import BytesIO
from calculator import calculate
from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

root = os.getcwd()

app = Flask(__name__)
api = Api(app)
CORS(app)

image_req_args = reqparse.RequestParser()
image_req_args.add_argument("image", type=str)

class Predict(Resource):
    
    def post(self):
        args = image_req_args.parse_args()
        if 'internals' in os.listdir():
            shutil.rmtree('internals')
        if 'segmented' in os.listdir():
            shutil.rmtree('segmented')
        os.mkdir('segmented')
        operation = BytesIO(base64.urlsafe_b64decode(args['image']))
        operation = main(operation)
        print("operation :", operation)
        print("solution :", calculate(operation))
        os.mkdir('internals')
        shutil.move('segmented', 'internals')
        shutil.move('input.png', 'internals')
        shutil.move('segmented_characters.csv', 'internals')
        formatted_equation, solution = calculate(operation)
        solution = " ".join(str(x) for x in solution)
        return json.dumps({
            'Entered_equation': operation,
            'Formatted_equation': formatted_equation,
            'solution': solution
        })

api.add_resource(Predict, "/predict")

if __name__ == "__main__":
    app.run(debug=True)