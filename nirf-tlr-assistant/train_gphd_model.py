import pandas as pd
import numpy as np
import joblib
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# ----------------------------------------
# 1. Load dataset
# ----------------------------------------
df = pd.read_excel("data/MasterData_GPHD.xlsx")

# ----------------------------------------
# 2. Feature Engineering
# ----------------------------------------
df["PhD_2021_22"] = df["Full_2021-22"] + df["Part_2021-22"]
df["PhD_2022_23"] = df["Full_2022-23"] + df["Part_2022-23"]
df["PhD_2023_24"] = df["Full_2023-24"] + df["Part_2023-24"]

df["Nphd"] = (
    df["PhD_2021_22"] +
    df["PhD_2022_23"] +
    df["PhD_2023_24"]
) / 3

# ----------------------------------------
# 3. Features & Target
# ----------------------------------------
X = df[["Nphd"]]
y = df["GPHD"]

# ----------------------------------------
# 4. Train-Test Split
# ----------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------------
# 5. XGBoost Model
# ----------------------------------------
model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.1,
    max_depth=3,
    objective="reg:squarederror",
    random_state=42
)

model.fit(X_train, y_train)

# ----------------------------------------
# 6. Evaluation
# ----------------------------------------
preds = model.predict(X_test)

print("R2 Score:", r2_score(y_test, preds))
rmse = np.sqrt(mean_squared_error(y_test, preds))
print("RMSE:", rmse)

# ----------------------------------------
# 7. Save Model
# ----------------------------------------
joblib.dump(model, "model/gphd_model.pkl")

print("✅ GPHD model saved as gphd_xgb_model.pkl")
