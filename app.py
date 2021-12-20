# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 13:56:57 2021

@author: lenovo
"""

import numpy as np
from flask import Flask,request,render_template
import pickle
import sklearn

app = Flask(__name__)
model=pickle.load(open('modelheart.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features)
    #temp=np.array([0,0,0,0,0,0,0,0,0,0])
    #a=np.append(final_features,temp)
    b=[final_features]
    prediction = model.predict(b)
    output = prediction[0]
    if output==1:
       output='High'
    elif output==0:
         output='No'
    return render_template('index.html', prediction_text='{} risk of getting Heart Diseases'.format(output))

if __name__ == "__main__":
   app.run(debug=True)
