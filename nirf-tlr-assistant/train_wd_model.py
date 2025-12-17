import pickle
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

# -------------------------------------------------------
# 1. Load Excel
# -------------------------------------------------------
df = pd.read_excel("data/MasterData_WD.xlsx")

# -------------------------------------------------------
# 2. Feature Engineering
# -------------------------------------------------------

# Total women students from all levels
df["Total_Women_Students"] = (
    df["NE_UG4_Female"] +
    df["NE_UG5_Female"] +
    df["NE_PG2_Female"]
)

df["Total_Students"] = (
    df["NE_UG4_Total"] +
    df["NE_UG5_Total"] +
    df["NE_PG2_Total"]
)

# Percentage of women students
df["NWS"] = (df["Total_Women_Students"] / df["Total_Students"]) * 100

# Use features for prediction
features = [
    "NE_UG4_Male", "NE_UG4_Female", "NE_UG4_Total",
    "NE_UG5_Male", "NE_UG5_Female", "NE_UG5_Total",
    "NE_PG2_Male", "NE_PG2_Female", "NE_PG2_Total",
    "NWS"
]

X = df[features]
y = df["WD"]     # target score

# -------------------------------------------------------
# 3. Train-Test Split
# -------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------------------------------
# 4. Train Model (Random Forest)
# -------------------------------------------------------
rf = RandomForestRegressor(n_estimators=300, random_state=42)
rf.fit(X_train, y_train)

# -------------------------------------------------------
# 5. Evaluate
# -------------------------------------------------------
pred = rf.predict(X_test)
print("R2 Score:", r2_score(y_test, pred))
print("MAE:", mean_absolute_error(y_test, pred))

# -------------------------------------------------------
# 6. Save Model
# -------------------------------------------------------
pickle.dump(rf, open("model/wd_model.pkl", "wb"))
print("Model saved as wd_model.pkl")
