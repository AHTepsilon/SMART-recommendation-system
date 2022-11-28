from flask import Flask, json, request, render_template, url_for, redirect
from flask_cors import CORS
import numpy as np
import pandas as pd
import math
import array as arr
from scipy.spatial import distance

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split

app = Flask(__name__)

df = pd.read_csv('data/db.csv')
  
  
# route to html page - "table"
@app.route('/')
@app.route('/table')
def table():
    
    # converting csv to html
    data = pd.read_csv('data/db.csv')
    return render_template('index.html', tables=[data.to_html()], titles=[''])
  

@app.route('/grupos', methods=['GET', 'POST'])
def grupos():
    data = pd.read_csv('data/db.csv')
    result = 1 - distance.cosine(data.DiegoMonteroRes, data.DianaBalantaRes)
    print("Distancia coseno:", result)
    return render_template('grupo.html')

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    return render_template('lista.html')
  
if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))