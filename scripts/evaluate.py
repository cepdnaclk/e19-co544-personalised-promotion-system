import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import load_model
import joblib

def evaluate():
    data = pd.read_csv('data/processed_data.csv')
    X = data.drop(columns=['Amount'])
    y = data['Amount']

    X_scaler = joblib.load('models/X_scaler.pkl')
    y_scaler = joblib.load('models/y_scaler.pkl')

    X_scaled = X_scaler.transform(X)
    y_scaled = y_scaler.transform(y.values.reshape(-1, 1))

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

    model = load_model('models/model.h5')

    loss = model.evaluate(X_test, y_test)
    print(f'Test Loss: {loss}')

    y_pred_scaled = model.predict(X_test)
    y_pred_original = y_scaler.inverse_transform(y_pred_scaled)
    y_test_original = y_scaler.inverse_transform(y_test)

    print(f'Predicted amounts (original scale): {y_pred_original[:5].flatten()}')
    print(f'Actual amounts (original scale): {y_test_original[:5].flatten()}')

if __name__ == "__main__":
    evaluate()
