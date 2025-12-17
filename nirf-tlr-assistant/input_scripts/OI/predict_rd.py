import torch
import pickle
import numpy as np
from train_rd_model import RDModel

MODEL_PATH = "model/RD_model.pth"
SCALER_PATH = "model/rd_scaler.pkl"

_model = None
_scaler = None

def load_model():
    global _model, _scaler
    
    if _model is None:
        _model = RDModel()
        _model.load_state_dict(
            torch.load(MODEL_PATH, map_location=torch.device("cpu"))
        )
        _model.eval()
    
    if _scaler is None:
        with open(SCALER_PATH, "rb") as f:
            _scaler = pickle.load(f)
    
    return _model, _scaler

def predict_rd(
    ug4_out_state, ug5_out_state, pg2_out_state,
    ug4_out_country, ug5_out_country, pg2_out_country,
    ug4_total, ug5_total, pg2_total
):
    model, scaler = load_model()
    
    # Aggregate values
    total_out_state = (
        ug4_out_state +
        ug5_out_state +
        pg2_out_state
    )
    
    total_out_country = (
        ug4_out_country +
        ug5_out_country +
        pg2_out_country
    )
    
    total_students = ug4_total + ug5_total + pg2_total
    if total_students == 0:
        total_students = 1
    
    fraction_state = total_out_state / total_students
    fraction_country = total_out_country / total_students
    
    # Feature vector
    X = np.array([[
        total_out_state,
        total_out_country,
        total_students,
        fraction_state,
        fraction_country
    ]])
    
    X_scaled = scaler.transform(X)
    X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
    
    with torch.no_grad():
        rd_score = model(X_tensor).item()
    
    return round(rd_score, 2)