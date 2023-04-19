from flask_bootstrap import Bootstrap4
from flask import Flask, render_template, jsonify, request
import tensorflow as tf
import json

app = Flask(__name__)
bootstrap = Bootstrap4(app)

@app.route("/")
def hello_world():
    return render_template('index.html', bootstrap=bootstrap)

@app.route('/analyze', methods= ['POST'])
def analyze():
    frequency = request.json['frequency']
    package = request.json['package']
    # frequency = request.get_json()
    model = tf.keras.models.load_model('yodlee_example')


    sample = {
      'Package': package,
      'Frequency': frequency
    }

    inputSample = {name: tf.convert_to_tensor(
        [value]) for name, value in sample.items()
    }


    prediction = model.predict(inputSample)
    p = tf.nn.sigmoid(prediction[0])

    predictPercent = int(p * 100)

    return jsonify(result=predictPercent)