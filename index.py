from flask_bootstrap import Bootstrap4
from flask import Flask, render_template, jsonify, request
import tensorflow as tf
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap4(app)

assessment_model = tf.keras.models.load_model('assessment_model')

@app.route("/")
def hello_world():
    return render_template('index.html', bootstrap=bootstrap)

@app.route("/assessment")
def assessment():
    return render_template('assessment.html', bootstrap=bootstrap)

@app.route('/analyze-assessment', methods=['POST'])
def analyzeAssessment():
    data = request.form
    
    prepareData = {
        "product": data['assess-product'],
        "source": data['assess-source'],
        "PPSRCheck": data["assess-ppsr"],
        "companyStructure": data["assess-company"],
        "bankStatementChecked": "True" if data["assess-bank-check"] == "1" else "False",
    }
    
    input_data = {name: tf.convert_to_tensor([value]) for name, value in prepareData.items()}
    
    prediction = assessment_model.predict(input_data)
    result = tf.nn.sigmoid(prediction[0])
    
    print(prepareData)
    print(result.numpy())
    
    responseText = 'APPROVE' if result.numpy() > 0.5 else 'DECLINED'
    
        
    return render_template('assessment-result.html', bootstrap=bootstrap, result=responseText)