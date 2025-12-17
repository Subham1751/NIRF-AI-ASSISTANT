import joblib
import pandas as pd

def load_model(model_path="model/ss_model.pkl"):
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def predict_ss(model, nt_total, ne_total, np_total):
    if nt_total < 0 or ne_total < 0 or np_total < 0:
        raise ValueError("NT, NE, NP values cannot be negative.")
    
    input_df = pd.DataFrame({
        "NT_total": [nt_total],
        "NE_total": [ne_total],
        "NP_total": [np_total]
    })
    
    prediction = model.predict(input_df)[0]
    
    return round(prediction, 3)

if __name__ == "__main__":
    print("\n--- SS Score Prediction Tool ---\n")
    
    model = load_model()
    if model is None:
        exit()
    
    nt = float(input("Enter NT_Total: "))
    ne = float(input("Enter NE_total: "))
    np = float(input("Enter NP_total: "))
    
    ss_score = predict_ss(model, nt, ne, np)
    
    print(f"\nPredicted SS Score: {ss_score}")