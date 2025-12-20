import pandas as pd
import joblib

MODEL_PATH = "model/gue_model.pkl"

_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_gue(
    ug4_intake1, ug4_passed1,
    ug4_intake2, ug4_passed2,
    ug4_intake3, ug4_passed3,

    ug5_intake1, ug5_passed1,
    ug5_intake2, ug5_passed2,
    ug5_intake3, ug5_passed3,

    pg2_intake1, pg2_passed1,
    pg2_intake2, pg2_passed2,
    pg2_intake3, pg2_passed3,

    pg3_intake1, pg3_passed1,
    pg3_intake2, pg3_passed2,
    pg3_intake3, pg3_passed3,
):
    total_intake = (
        ug4_intake1 + ug4_intake2 + ug4_intake3 +
        ug5_intake1 + ug5_intake2 + ug5_intake3 +
        pg2_intake1 + pg2_intake2 + pg2_intake3 +
        pg3_intake1 + pg3_intake2 + pg3_intake3
    )
    
    total_graduated = (
        ug4_passed1 + ug4_passed2 + ug4_passed3 +
        ug5_passed1 + ug5_passed2 + ug5_passed3 +
        pg2_passed1 + pg2_passed2 + pg2_passed3 +
        pg3_passed1 + pg2_passed2 + pg2_passed3
    )
    
    if total_intake == 0:
        return 0.0
    
    Ng = (total_graduated / total_intake) * 100
    gue_formula = 15 * min(Ng / 80, 1)
    
    X = pd.DataFrame([{
        "Ng": Ng,
        "Ng_over_80": Ng / 80,
        "Total_Intake": total_intake,
        "Total_Graduate": total_graduated
    }])
    
    model = load_model()
    residual = model.predict(X)[0]
    
    gue_score = gue_formula + residual
    
    gue_score = max(0.0, min(15.0, gue_score))
    return round(gue_score, 2), total_intake, total_graduated, Ng