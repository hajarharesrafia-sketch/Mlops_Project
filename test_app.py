import os
import joblib

def test_model_file_exists():
    assert os.path.exists("model.pkl"), "Model file does not exist"

def test_model_load():
    model = joblib.load("model.pkl")
    assert model is not None, "Model failed to load"

def test_prediction():
    model = joblib.load("model.pkl")

    sample = [[68, 150, 195, 0.0, 1, 132]]  # même ordre que ton dataset
    prediction = model.predict(sample)

    assert prediction is not None
    