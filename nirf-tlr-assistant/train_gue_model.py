import pandas as pd
import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# =====================================
# LOAD EXCEL DATA
# =====================================
df = pd.read_excel("data/MasterData_GUE.xlsx")

# =====================================
# COMPUTE Ng (OFFICIAL NIRF DEFINITION)
# =====================================
def compute_ng(row):
    total_intake = row.filter(like="INTAKE").sum()
    total_graduates = row.filter(like="GRADUATE").sum()

    if total_intake == 0:
        return 0

    return (total_graduates / total_intake) * 100

df["Ng"] = df.apply(compute_ng, axis=1)

# =====================================
# BASELINE FORMULA GUE
# =====================================
df["Ng_over_80"] = df["Ng"] / 80
df["Ng_capped"] = df["Ng_over_80"].clip(upper=1)
df["GUE_formula"] = 15 * df["Ng_capped"]

# =====================================
# TARGET = HIDDEN ADJUSTMENT
# =====================================
df["GUE_residual"] = df["GUE"] - df["GUE_formula"]

# =====================================
# FEATURES (CLEAN & MEANINGFUL)
# =====================================
X = pd.DataFrame({
    "Ng": df["Ng"],
    "Ng_over_80": df["Ng_over_80"],
    "Total_Intake": df.filter(like="INTAKE").sum(axis=1),
    "Total_Graduate": df.filter(like="GRADUATE").sum(axis=1)
})

y = df["GUE_residual"]

# =====================================
# TRAIN / TEST SPLIT
# =====================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================================
# XGBOOST MODEL
# =====================================
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

model.fit(X_train, y_train)

# =====================================
# EVALUATION (FINAL GUE)
# =====================================
residual_pred = model.predict(X_test)

gue_formula_test = df.loc[X_test.index, "GUE_formula"]
gue_final_pred = gue_formula_test + residual_pred
gue_actual = df.loc[X_test.index, "GUE"]

print("\n📊 FINAL GUE MODEL PERFORMANCE")
print("R² Score:", round(r2_score(gue_actual, gue_final_pred), 4))
print("MAE:", round(mean_absolute_error(gue_actual, gue_final_pred), 4))

# =====================================
# SAVE MODEL
# =====================================
joblib.dump(model, "model/gue_model.pkl")
print("\n✅ Model saved as gue_xgboost_residual_model.pkl")