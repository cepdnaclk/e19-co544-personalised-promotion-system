from flask import Flask, request, jsonify
import pandas as pd
import joblib
from promotions import get_spend_type, get_promotion

app = Flask(__name__)

# Load the pre-trained K-Modes model
kmodes_model = joblib.load('../pkl files/model_with_12_clusters.pkl')

# Define feature decoding dictionaries
month_decoding = {
    0: "January", 1: "February", 2: "March", 3: "April", 4: "May",
    5: "June", 6: "July", 7: "August", 8: "September", 9: "October",
    10: "November", 11: "December"
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    month = data.get('month')
    feature1 = data.get('feature1')
    feature2 = data.get('feature2')

    if month not in month_decoding.values():
        return jsonify({"error": "Invalid month"}), 400

    # Encode the month input
    month_code = list(month_decoding.keys())[list(month_decoding.values()).index(month)]
    
    # Create DataFrame for prediction
    input_data = {
        'feature1': [feature1],
        'feature2': [feature2],
        'month': [month_code]
    }
    
    df = pd.DataFrame(input_data)

    # Predict the cluster
    cluster = kmodes_model.predict(df)[0]

    # Get spend type based on the cluster
    spend_type = get_spend_type(cluster)

    # Get promotion based on the spend type
    promotion = get_promotion(spend_type)

    return jsonify({"cluster": int(cluster), "spend_type": spend_type, "promotion": promotion})

if __name__ == '__main__':
    app.run(debug=True)
