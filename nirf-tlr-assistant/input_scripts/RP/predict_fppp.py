import pandas as pd
import joblib

MODEL_PATH = "model/fppp_model.pkl"

_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_fppp(
    spon_amt_24, spon_amt_23, spon_amt_22,
    consul_amt_24, consul_amt_23, consul_amt_22,
    total_fac
):
    model = load_model()
    
    if total_fac <= 0:
        return 0.0
    
    avg_rf = (spon_amt_24 + spon_amt_23 + spon_amt_22) / 3
    avg_cf = (consul_amt_24 + consul_amt_23 + consul_amt_22) / 3
    
    rf_per_faculty = avg_rf / total_fac
    cf_per_faculty = avg_cf / total_fac
    
    data = {
        "RF_per_faculty": rf_per_faculty,
        "CF_per_faculty": cf_per_faculty
    }
    
    df_input = pd.DataFrame([data])
    score = model.predict(df_input)[0]
    score = max(0.0, min(10.0, score))
    
    return round(float(score), 2)
    