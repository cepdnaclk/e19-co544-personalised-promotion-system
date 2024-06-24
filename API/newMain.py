from flask import Flask, request, jsonify
from joblib import Parallel, delayed 
import joblib 
import pandas as pd

# Load the trained K-Modes model
knn_from_joblib = joblib.load('../pkl files/model_with_12_clusters.pkl') 

print("Loaded successfully!")

app = Flask(__name__)

@app.route('/clusters', methods=['GET'])
def get_clusters():
    cluster_centers = knn_from_joblib.cluster_centroids_
    return jsonify({'cluster_centers': cluster_centers.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
