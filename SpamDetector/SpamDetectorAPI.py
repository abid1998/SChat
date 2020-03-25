from flask import Flask, jsonify, request
from sklearn.externals import joblib
from nltk.corpus import stopwords
import string
app = Flask(__name__)


def text_process(mess):
    """
    1. Remove Punc
    2. Remove Stop words
    3. Return list of clean text words
    """

    nopunc = [char for char in mess if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


@app.route('/spam', methods=['POST'])
def predict():
    print(request)
    req_json = request.get_json()
    print(req_json)
    query = req_json["text"]
    query = [query]
    prediction = list(lr.predict(query))
    return jsonify({"prediction": prediction})


if __name__ == '__main__':
    lr = joblib.load("output.pkl")  # Load the ML model
    print('Model loaded')

    app.run(port=8000, debug=True)
