from flask import Flask, request
from flask_restful import Resource, Api
from model import myBert, myHMM
from flask import jsonify

app = Flask(__name__)
api = Api(app)

todos = {}
HMM = myHMM()

class Predictability(Resource):
    def get(self):
        # sentence  = request.form['data']  or 'I like to eat apples'
        sentence  = 'I like to eat apples'
        Bert = myBert()
        result = Bert.get_probabilities(sentence)
        return jsonify(sentence = result)

class HMMPredict(Resource):
    def get(self):
        words = '' # request.form['data']
        result = HMM.get_words(words)
        return jsonify(sentence = result)


api.add_resource(Predictability, '/')
api.add_resource(HMMPredict, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
