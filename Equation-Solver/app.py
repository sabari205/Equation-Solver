import os
import json
import base64
import shutil
from main import main
from io import BytesIO
from calculator import calculate
from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS

#port = int(os.environ.get('PORT', 5000))
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
        print(operation)
        operation = main(operation)
        print("operation :", operation)
        print("solution :", calculate(operation))
        os.mkdir('internals')
        shutil.move('segmented', 'internals')
        shutil.move('input.png', 'internals')
        if 'segmented_characters.csv' not in os.listdir():
            return json.dumps({
            'Entered_equation': '',
            'Formatted_equation': '',
            'solution': ''
        })

        shutil.move('segmented_characters.csv', 'internals')
        formatted_equation, solution = calculate(operation)
#        solution = " ".join(str(x) for x in solution)
        return json.dumps({
            'Entered_equation': operation,
            'Formatted_equation': formatted_equation,
            'solution': solution
        })

@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Equations Solver</h1>"

api.add_resource(Predict, "/predict")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
