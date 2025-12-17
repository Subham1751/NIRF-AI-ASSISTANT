import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, r2_score

def train_ss_model(input_path: str, model_output_path: str):
    # STEP 1: Load data
    print("\nSTEP 1: Loading data...")
    df = pd.read_csv(input_path)
    print(f"Loaded {len(df)} records")
    
    feature_cols = [
        "NT_total",
        "NE_total",
        "NP_total",
    ]
    
    # STEP 2: Check for missing values
    print("\nSTEP 2: Checking for missing values...")
    X = df[feature_cols]
    y = df["SS_Score"]
    
    print(f"Missing values per feature:")
    missing_counts = X.isnull().sum()
    for col, count in missing_counts.items():
        if count > 0:
            print(f"{col}: {count} missing")
    
    print(f"\nMissing values in target (SS_Score): {y.isnull().sum()}")
    
    # STEP 3: Handle missing values
    print("\nSTEP 3: Handling missing values...")
    # Drop rows where target is missing
    valid_idx = y.notna()
    X = X[valid_idx]
    y = y[valid_idx]
    
    # Drop rows with missing NT, NE, NP
    missing_before = len(X)
    df_clean = pd.concat([X, y], axis=1).dropna()
    X = df_clean[feature_cols]
    y = df_clean["SS_Score"]

    print(f"Dropped {missing_before - len(X)} rows due to missing core values.")
    
    print(f"Data cleaned. Shape: {X.shape}")
    print(f"Remaining NaN values: {X.isnull().sum().sum()}")
    
    print(f"Data cleaned. Shape: {X.shape}")
    print(f"Remaining NaN values: {X.isnull().sum().sum()}")
    
    # STEP 4: Split data
    print("\nSTEP 4: Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    print(f"Training set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")
    
    # STEP 5: Train model
    print("\nSTEP 5: Training model...")
    model = GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=3
    )
    
    model.fit(X_train, y_train)
    print("Model trained successfully!")
    
    # STEP 6: Evaluate
    print("\nSTEP 6: Evaluating model...")
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n--- SS Model Performance ---")
    print(f"MAE: {mae: .3f}")
    print(f"R2 Score: {r2: .3f}")
    
    joblib.dump(model, model_output_path)
    print(f"Model saved to {model_output_path}")
    
    return model

if __name__ == "__main__":
    train_ss_model(
        input_path="data/ss_feature_engineered.csv",
        model_output_path="model/ss_model.pkl"
    )