import pandas as pd
import joblib

MODEL_PATH = "model/gphd_model.pkl"
_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_gphd(
    tot_fphd_23, tot_fphd_22, tot_fphd_21,
    tot_pphd_23, tot_pphd_22, tot_pphd_21
):
    model = load_model()
    
    phd_23 = tot_fphd_23 + tot_pphd_23
    phd_22 = tot_fphd_22 + tot_pphd_22
    phd_21 = tot_fphd_21 + tot_pphd_21
    
    nphd = (phd_23 + phd_22 + phd_21) / 3
    
    df_input = pd.DataFrame([{
        "Nphd": nphd
    }])
    
    score = model.predict(df_input)[0]
    return round(float(score), 2)