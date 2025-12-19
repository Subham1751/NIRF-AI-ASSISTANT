import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
import joblib

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_excel("GMS.xlsx")

# -----------------------------
# Feature Columns
# -----------------------------
feature_cols = [
    'UG4_PLACED_MEDIAN_SALARY_2021-22',
    'UG4_PLACED_MEDIAN_SALARY_2022-23',
    'UG4_PLACED_MEDIAN_SALARY_2023-24',
    'UG5_PLACED_MEDIAN_SALARY_2021-22',
    'UG5_PLACED_MEDIAN_SALARY_2022-23',
    'UG5_PLACED_MEDIAN_SALARY_2023-24',
    'PG2_PLACED_MEDIAN_SALARY_2021-22',
    'PG2_PLACED_MEDIAN_SALARY_2022-23',
    'PG2_PLACED_MEDIAN_SALARY_2023-24',
    'PG3_PLACED_MEDIAN_SALARY_2021-22',
    'PG3_PLACED_MEDIAN_SALARY_2022-23',
    'PG3_PLACED_MEDIAN_SALARY_2023-24',
    'PG5_PLACED_MEDIAN_SALARY_2021-22',
    'PG5_PLACED_MEDIAN_SALARY_2022-23',
    'PG5_PLACED_MEDIAN_SALARY_2023-24'
]

X = df[feature_cols]
y = df['MS']   # Official NIRF GMS score

# -----------------------------
# Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# XGBoost Model
# -----------------------------
model = XGBRegressor(
    n_estimators=300,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Evaluation
# -----------------------------
y_pred = model.predict(X_test)

print("R² Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "model/gms_model.pkl")
print("✅ Model saved as gms_model.pkl")
