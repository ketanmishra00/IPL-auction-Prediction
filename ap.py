# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 01:35:05 2021

@author: Ketan
"""
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle 
import flasgger
from flasgger import Swagger

app=Flask(__name__)

app=Flask(__name__)
pickle_in=open('mod.pkl','rb')
model = pickle.load(pickle_in)

@app.route('/')
def predict_ipl_auction():
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      
      - name: Inns
        in: query
        type: number
        required: true
      - name: Runs
        in: query
        type: number
        required: true
      - name: Avg
        in: query
        type: number
        required: true
      - name: SR
        in: query
        type: number
        required: true
      - name: Eskill
        in: query
        type: number
        required: true
      - name: form
        in: query
        type: number
        required: true
      - name: country
        in: query
        type: number
        required: true
     
      - name: hundred
        in: query
        type: number
        required: true
        
    responses:
        200:
            description: The output values
        
    """

    Inns=request.args.get("Inns")

    Runs=request.args.get("Runs")
    Avg=request.args.get("Avg")
    SR=request.args.get("SR")
    Eskill=request.args.get("Eskill")
    form=request.args.get("form")
    country=request.args.get("country")
 
    hundred=request.args.get("hundred")
    prediction=model.predict([[Inns,Runs,Avg,SR,Eskill,form,country,hundred]])
    print(prediction)
    return"The price is player in crore" + str(prediction)



if __name__=='__main__':
    app.run()