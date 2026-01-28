# ---------------------------------------------------
#   COMPLETE ESCS PREDICTION MODEL (TRAIN + TEST)
#   WITH NaN IMPUTATION FIX
# ---------------------------------------------------

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.impute import SimpleImputer
import numpy as np

MODEL_PATH = "model/escs_model.pkl"
IMPUTER_PATH = "model/escs_imputer.pkl"

_model = None
_imputer = None

# ---------------------------------------------------
# 1. LOAD YOUR EXCEL DATA
# ---------------------------------------------------
df = pd.read_excel("data/Engineering/MasterData_ESCS.xlsx", engine="openpyxl")

# ---------------------------------------------------
# 2. REPLACE NaN WITH 0 OR MEAN
# ---------------------------------------------------
# For fee reimbursement, missing = 0 makes sense
df = df.fillna(0)

# ---------------------------------------------------
# 3. FEATURE ENGINEERING
# ---------------------------------------------------
df["UG4_reimb_total"] = df["NE_UG4_FeeReimb_State"] + df["NE_UG4_FeeReimb_Institute"]
df["UG5_reimb_total"] = df["NE_UG5_FeeReimb_State"] + df["NE_UG5_FeeReimb_Institute"]
df["UG_total"] = df["UG4_total"] + df["UG5_Total"]

# Avoid division by zero
df["UG_total"] = df["UG_total"].replace(0, 1)

df["Nesc"] = (df["UG4_reimb_total"] + df["UG5_reimb_total"]) / df["UG_total"]

# ---------------------------------------------------
# 4. SELECT FEATURES AND LABEL
# ---------------------------------------------------
X = df[[
    "NE_UG4_FeeReimb_State",
    "NE_UG4_FeeReimb_Institute",
    "NE_UG5_FeeReimb_State",
    "NE_UG5_FeeReimb_Institute",
    "UG4_reimb_total",
    "UG5_reimb_total",
    "UG_total",
    "Nesc"
]]

y = df["ESCS"]

# ---------------------------------------------------
# 5. IMPUTE ANY REMAINING NaN JUST IN CASE
# ---------------------------------------------------
imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

# ---------------------------------------------------
# 6. TRAIN-TEST SPLIT
# ---------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------
# 7. MODEL TRAINING
# ---------------------------------------------------
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# ---------------------------------------------------
# 8. TESTING & ACCURACY
# ---------------------------------------------------
preds = model.predict(X_test)

# print("\n====== MODEL ACCURACY ======")
# print("R2 Score:", r2_score(y_test, preds))
# print("MSE:", mean_squared_error(y_test, preds))
rmse = np.sqrt(mean_squared_error(y_test, preds))
# print("RMSE:", rmse)
#print("RMSE:", mean_squared_error(y_test, preds, squared=False))

# ---------------------------------------------------
# 9. SAVE MODEL
# ---------------------------------------------------
joblib.dump(model, "model/escs_model.pkl")
joblib.dump(imputer, "model/escs_imputer.pkl")

# ---------------------------------------------------
# 10. USER INPUT PREDICTION FUNCTION
# ---------------------------------------------------
def predict_escc(state4, inst4, tot4, state5, inst5, tot5):
    print("\n======= ESCS PREDICTOR =======")
    global _model, _imputer
    
    if _model is None or _imputer is None:
        _model = joblib.load(MODEL_PATH)
        _imputer = joblib.load(IMPUTER_PATH)

    # state4 = float(input("UG4 Fee Reimbursed by State: "))
    # inst4 = float(input("UG4 Fee Reimbursed by Institute: "))
    # tot4 = float(input("UG4 Total Students: "))

    # state5 = float(input("UG5 Fee Reimbursed by State: "))
    # inst5 = float(input("UG5 Fee Reimbursed by Institute: "))
    # tot5 = float(input("UG5 Total Students: "))

    # Features
    ug4_reimb = state4 + inst4
    ug5_reimb = state5 + inst5
    ug_total = tot4 + tot5

    if ug_total == 0:
        ug_total = 1

    nesc = (ug4_reimb + ug5_reimb) / ug_total

    x_new = [[
        state4, inst4, state5, inst5,
        ug4_reimb, ug5_reimb, ug_total, nesc
    ]]

    # Apply same imputer
    x_new = imputer.transform(x_new)

    escs_score = model.predict(x_new)[0]
#    print("ESCS Score: ", round(escs_score, 2))
    return round(escs_score, 2)
