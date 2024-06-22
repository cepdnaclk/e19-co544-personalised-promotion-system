from scripts.preprocess import preprocess
import os

def test_preprocess():
    preprocess()
    assert os.path.exists('data/processed_data.csv')

if __name__ == "__main__":
    test_preprocess()
