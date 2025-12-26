import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

DEFAULT_EXCEL_PATH = "data/MasterData_FPPP.xlsx"
MODEL_OUT_PATH = "model/fppp_model.pkl"
META_OUT_PATH = "model/fppp_model_meta.pkl"
RANDOM_STATE = 42

def load_fppp_master(excel_path: str) -> pd.DataFrame:
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Master Excel not found: {excel_path}")
    
    df = pd.read_excel(excel_path)
    df.columns = [c.strip() for c in df.columns]
    return df

def feature_engineer_fppp(df: pd.DataFrame) -> pd.DataFrame:
    required_cols = [
        "FPPP_Score",
        "Total_Faculties",
        "Spon_Total_Amount_2023-24",
        "Spon_Total_Amount_2022-23",
        "Spon_Total_Amount_2021-22",
        "Consul_Total_Amount_2023-24",
        "Consul_Total_Amount_2022-23",
        "Consul_Total_Amount_2021-22",
    ]
    
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns in master sheet: {missing}")

    for c in required_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    
    df = df[df["Total_Faculties"].notna() & (df["Total_Faculties"] > 0)]
    df = df[df["FPPP_Score"].notna()]
    
    df["RF_avg_3yr"] = (
        df["Spon_Total_Amount_2023-24"] +
        df["Spon_Total_Amount_2022-23"] +
        df["Spon_Total_Amount_2021-22"]
    ) / 3.0
    
    df["CF_avg_3yr"] = (
        df["Consul_Total_Amount_2023-24"] +
        df["Consul_Total_Amount_2022-23"] +
        df["Consul_Total_Amount_2021-22"]
    ) / 3.0
    
    df["RF_per_faculty"] = df["RF_avg_3yr"] / df["Total_Faculties"]
    df["CF_per_faculty"] = df["CF_avg_3yr"] / df["Total_Faculties"]
    
    out = df[["RF_per_faculty", "CF_per_faculty", "FPPP_Score"]].copy()
    
    out = out.replace([float("inf"), float("-inf")], pd.NA).dropna()
    
    return out

def train_fppp_model(
    excel_path: str = DEFAULT_EXCEL_PATH,
    model_out_path: str = MODEL_OUT_PATH,
    meta_out_paht: str = META_OUT_PATH
):
    print("STEP 1: Loading master data...")
    df = load_fppp_master(excel_path)
    
    print("Step 2: Feature engineering...")
    fe_df = feature_engineer_fppp(df)
    
    feature_cols = ["RF_per_faculty", "CF_per_faculty"]
    target_col = "FPPP_Score"
    
    X = fe_df[feature_cols].values
    y = fe_df[target_col].values
    
    print(f"Rows after cleaning: {len(fe_df)}")
    if len(fe_df) < 20:
        print("WARNING: Very few rows for training. Model may be unstable.")
    
    print("STEP 3: Train/test split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=RANDOM_STATE
    )
    
    print("STEP 4: Training mdodel...")
    model = GradientBoostingRegressor(random_state=RANDOM_STATE)
    model.fit(X_train, y_train)
    
    print("STEP 5: Evaluating model...")
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n--- FPPP Model Performance ---")
    print(f"MAE: {mae:.3f}")
    print(f"R2: {r2:.3f}")
    
    print("STEP 6: Saving model + metadata...")
    os.makedirs(os.path.dirname(model_out_path), exist_ok=True)
    
    joblib.dump(model, model_out_path)
    joblib.dump(
        {
            "feature_cols": feature_cols,
            "target_col": target_col,
            "excel_path": excel_path,
        },
        meta_out_paht,
    )
    
    print(f"\nSaved model to: {model_out_path}")
    print(f"Saved metadata to: {meta_out_paht}")
    
    return model

if __name__=="__main__":
    train_fppp_model()