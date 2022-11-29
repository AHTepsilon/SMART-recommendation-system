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

    array_1 = []
    array_2 = []
    array_3 = []
    array_4 = []
    array_5 = []
    array_6 = []
    array_7 = []
    array_8 = []
    array_9 = []
    array_10 = []
    array_11 = []
    array_12 = []
    array_13 = []
    array_14 = []
    array_15 = []
    array_16 = []
    array_17 = []
    array_18 = []

    for i in data.Andrea_Diaz:
        array_1.append(i)
    
    for i in data.Angela_Campuzano:
        array_2.append(i)
        
    for i in data.Catherine_Trujillo:
        array_3.append(i)
        
    for i in data.Daniela_Valencia:
        array_4.append(i)
        
    for i in data.Diana_Balanta:
        array_5.append(i)

    for i in data.Diego_Montero:
        array_6.append(i)
        
    for i in data.Laura_Fajardo:
        array_7.append(i)
        
    for i in data.Laura_Mosquera:
        array_8.append(i)

    for i in data.Laura_Orozco:
        array_9.append(i)
        
    for i in data.Laura_Reyes:
        array_10.append(i)

    for i in data.Laura_Tangarife:
        array_11.append(i)
        
    for i in data.Maria_Polanco:
        array_12.append(i)
        
    for i in data.Mateo_Martinez:
        array_13.append(i)
        
    for i in data.Santiago_Gutierrez:
        array_14.append(i)

    for i in data.Sara_Calderon:
        array_15.append(i)
        
    for i in data.Sara_Castillo:
        array_16.append(i)
        
    for i in data.Valentina_Grisales:
        array_17.append(i)

    for i in data.Valentina_Mueses:
        array_18.append(i)

    X = [array_1, array_2, array_3, array_4, array_5, array_6, array_7, array_8, array_9, array_10, array_11, array_12, array_13, array_14, array_15, array_16, array_17, array_18]

    select = request.args.get('name-select')
    result = 1 - distance.cosine(data.Diego_Montero, data.Diana_Balanta)
    arbitrary_value = math.sqrt(18) #Valor arbitrario, raíz cuadrada del número total de usuarios
    print(data.iloc[0])
    print("Distancia coseno:", result)
    print("Valor Arbitrario:", arbitrary_value)
    nbrs = NearestNeighbors(n_neighbors=10, algorithm='ball_tree').fit(X)
    distances, indices = nbrs.kneighbors(X)
    print("Distancias dentro del vecindario")
    i = 0
    for item in distances:
        print("Distancias de los usuarios con respecto al usuario ", i, "\n", item)
        i += 1
    f = 0
    for item in indices:
        print("Índices de los usuarios con respecto al usuario ", f, " (Ordenados del más cercano al más lejano)", "\n", item)
        f += 1
    return render_template('grupo.html')
    

@app.route('/lista', methods=['GET', 'POST'])
def lista():
    return render_template('lista.html')
  
if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))