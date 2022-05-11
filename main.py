from distutils.log import debug
from flask import Flask, jsonify , request
import pickle
import numpy as np
import pandas as pd
import sklearn as sd


model = pickle.load(open('bank_app.pkl', 'rb'))





app = Flask(__name__)
@app.route("/")
def hello():
    return   "Hello world"


@app.route('/predict', methods=['POST'])
def predict():
    CreditScore = request.form.get('Credit Score')
    Age = request.form.get('Age')
    Tenure = request.form.get('Tenure')
    Balance = request.form.get('Balance')
    NumberofProducts = request.form.get('Number of Products')
    HaveCreditCard = request.form.get('Have Credit Card?')
    ActiveMember = request.form.get('Active Member?')
    EstimatedSalary = request.form.get('Estimated Salary')

    input_query = np.array([[CreditScore, Age, Tenure, Balance, NumberofProducts, HaveCreditCard, ActiveMember, EstimatedSalary]])

    result = model.predict(input_query)[0]

    return jsonify({'stay': str(result)})




if __name__ ==  "__main__":

    app.run()
   