import pandas as pd
import joblib

MODEL_PATH = "model/gue_model.pkl"

_model = None

def load_model():
    global _model
    if _model is None:
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_gue():
    pass

# # =====================================
# # COMPUTE Ng (NIRF DEFINITION)
# # =====================================
# def compute_ng(row):
#     total_intake = row.filter(like="INTAKE").sum()
#     total_graduates = row.filter(like="GRADUATE").sum()

#     if total_intake == 0:
#         return 0

#     return (total_graduates / total_intake) * 100

# df["Ng"] = df.apply(compute_ng, axis=1)

# # =====================================
# # FORMULA GUE
# # =====================================
# df["Ng_over_80"] = df["Ng"] / 80
# df["Ng_capped"] = df["Ng_over_80"].clip(upper=1)
# df["GUE_formula"] = 15 * df["Ng_capped"]

# # =====================================
# # FEATURES FOR MODEL
# # =====================================
# X = pd.DataFrame({
#     "Ng": df["Ng"],
#     "Ng_over_80": df["Ng_over_80"],
#     "Total_Intake": df.filter(like="INTAKE").sum(axis=1),
#     "Total_Graduate": df.filter(like="GRADUATE").sum(axis=1)
# })

# # =====================================
# # LOAD TRAINED MODEL
# # =====================================
# model = joblib.load("gue_xgboost_residual_model.pkl")

# # =====================================
# # PREDICT RESIDUAL & FINAL GUE
# # =====================================
# df["GUE_residual_predicted"] = model.predict(X)
# df["GUE_Predicted"] = df["GUE_formula"] + df["GUE_residual_predicted"]

# # Optional safety cap
# df["GUE_Predicted"] = df["GUE_Predicted"].clip(0, 15)

# # =====================================
# # SAVE RESULTS
# # =====================================
# df.to_excel("top_100_gue_with_predictions.xlsx", index=False)

# print("✅ Prediction completed")
# print("📄 Output saved as: top_100_gue_with_predictions.xlsx")
