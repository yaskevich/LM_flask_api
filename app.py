from flask import Flask, request
from flask_restful import Resource, Api
from model import myBert
from flask import jsonify

app = Flask(__name__)
api = Api(app)

todos = {}

class Predictability(Resource):
    def get(self):
        sentence  = request.form['data']
        Bert = myBert()
        result = Bert.get_probabilities(sentence)
        return jsonify(sentence = result)

api.add_resource(Predictability, '/')

if __name__ == '__main__':
    app.run(debug=True)
