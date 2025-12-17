import pickle
import pandas as pd

MODEL_PATH = "model/wd_model.pkl"

_model = None

def load_model():
    global _model
    if _model is None:
        _model = pickle.load(open(MODEL_PATH, "rb"))
    return _model

def predict_wd(
    ug4_male, ug4_female, ug4_total,
    ug5_male, ug5_female, ug5_total,
    pg2_male, pg2_female, pg2_total,
):
    model = load_model()
    
    total_female_students = ug4_female + ug5_female + pg2_female
    total_students = ug4_total + ug5_total + pg2_total
    
    if total_students == 0:
        total_students = 1
    
    nws = (total_female_students / total_students) * 100
    
    X = pd.DataFrame([[
        ug4_male, ug4_female, ug4_total,
        ug5_male, ug5_female, ug5_total,
        pg2_male, pg2_female, pg2_total,
        nws
    ]], columns=[
        "NE_UG4_Male", "NE_UG4_Female", "NE_UG4_Total",
        "NE_UG5_Male", "NE_UG5_Female", "NE_UG5_Total",
        "NE_PG2_Male", "NE_PG2_Female", "NE_PG2_Total",
        "NWS"
    ])
    
    wd_score = model.predict(X)[0]
    return round(float(wd_score), 2)