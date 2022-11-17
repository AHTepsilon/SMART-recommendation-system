from flask import Flask
import numpy as np
import pandas as pd
import math
import array as arr
from flask import json, flask, request
from flask_cors import CORS
from scipy.spatial import distance

import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split

app = Flask(__name__)
CORS(app)

data_base = pd.read_csv('data/database.csv', encoding="utf-8")

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"