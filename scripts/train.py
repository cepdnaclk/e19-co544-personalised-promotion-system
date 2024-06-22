import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.regularizers import l2
import joblib

def train():
    data = pd.read_csv('data/processed_data.csv')
    X = data.drop(columns=['Amount'])
    y = data['Amount']

    X_scaler = StandardScaler()
    y_scaler = StandardScaler()

    X_scaled = X_scaler.fit_transform(X)
    y_scaled = y_scaler.fit_transform(y.values.reshape(-1, 1))

    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

    model = Sequential([
        Dense(256, input_dim=X_train.shape[1], activation='relu', kernel_regularizer=l2(0.001)),
        BatchNormalization(),
        Dropout(0.3),
        Dense(128, activation='relu', kernel_regularizer=l2(0.001)),
        BatchNormalization(),
        Dropout(0.3),
        Dense(64, activation='relu', kernel_regularizer=l2(0.001)),
        BatchNormalization(),
        Dropout(0.3),
        Dense(32, activation='relu', kernel_regularizer=l2(0.001)),
        BatchNormalization(),
        Dropout(0.3),
        Dense(1)
    ])

    model.compile(optimizer=Adam(learning_rate=0.0001), loss='mean_squared_error')

    early_stopping = EarlyStopping(monitor='val_loss', patience=20, restore_best_weights=True)
    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, min_lr=0.00001)

    history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=200, batch_size=64, callbacks=[early_stopping, reduce_lr])

    model.save('models/model.h5')
    joblib.dump(X_scaler, 'models/X_scaler.pkl')
    joblib.dump(y_scaler, 'models/y_scaler.pkl')

if __name__ == "__main__":
    train()
