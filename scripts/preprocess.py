import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess():
    data = pd.read_csv('data/dataset.csv').drop('index', axis=1)
    data['Date'] = pd.to_datetime(data['Date'], format='%d-%b-%y')
    data['Year'] = data['Date'].dt.year
    data['Month'] = data['Date'].dt.month
    data['Day'] = data['Date'].dt.day
    data = data.drop(columns=['Date'])
    
    categorical_columns = ['City', 'Card Type', 'Exp Type', 'Gender']
    label_encoders = {}
    for col in categorical_columns:
        label_encoders[col] = LabelEncoder()
        data[col] = label_encoders[col].fit_transform(data[col])
    
    data.to_csv('data/processed_data.csv', index=False)

if __name__ == "__main__":
    preprocess()
