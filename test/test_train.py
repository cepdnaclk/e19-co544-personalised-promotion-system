from scripts.train import train
import os

def test_train():
    train()
    assert os.path.exists('models/model.h5')
    assert os.path.exists('models/X_scaler.pkl')
    assert os.path.exists('models/y_scaler.pkl')

if __name__ == "__main__":
    test_train()
