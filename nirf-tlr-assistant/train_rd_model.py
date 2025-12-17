# train_rd.py
import pandas as pd
import torch
import torch.nn as nn
import pickle
from sklearn.preprocessing import StandardScaler

# ---------------------------------------------
# LOAD DATA
# ---------------------------------------------
df = pd.read_excel("data/MasterData_RD.xlsx")
df.columns = df.columns.str.strip()

# ---------------------------------------------
# CALCULATE TOTAL OUTSIDE STATE & OUTSIDE COUNTRY
# ---------------------------------------------
df["TOTAL_OUTSIDE_STATE"] = (
    df["NE_UG4_OutsideState"] +
    df["NE_UG5_OutsideState"] +
    df["NE_PG2_OutsideState"]
)

df["TOTAL_OUTSIDE_COUNTRY"] = (
    df["NE_UG4_OutsideCountry"] +
    df["NE_UG5_OutsideCountry"] +
    df["NE_PG2_OutsideCountry"]
)

df["TOTAL_STUDENTS"] = (
    df["NE_UG4_Total"] +
    df["NE_UG5_Total"] +
    df["NE_PG2_Total"]
)

# Avoid divide by zero
df["TOTAL_STUDENTS"] = df["TOTAL_STUDENTS"].replace(0, 1)

# ---------------------------------------------
# FEATURES BASED ON FORMULA
# ---------------------------------------------
df["fraction_state"] = df["TOTAL_OUTSIDE_STATE"] / df["TOTAL_STUDENTS"]
df["fraction_country"] = df["TOTAL_OUTSIDE_COUNTRY"] / df["TOTAL_STUDENTS"]

# Target variable (RD score, already present)
y = df["RD"]

# ML Input features
X = df[[
    "TOTAL_OUTSIDE_STATE",
    "TOTAL_OUTSIDE_COUNTRY",
    "TOTAL_STUDENTS",
    "fraction_state",
    "fraction_country"
]]

# ---------------------------------------------
# SCALING
# ---------------------------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save scaler
with open("model/rd_scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

# Convert to tensor
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

# ---------------------------------------------
# NEURAL NETWORK MODEL
# ---------------------------------------------
class RDModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(5, 16),
            nn.ReLU(),
            nn.Linear(16, 12),
            nn.ReLU(),
            nn.Linear(12, 8),
            nn.ReLU(),
            nn.Linear(8, 1)
        )

    def forward(self, x):
        return self.net(x)

model = RDModel()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
loss_fn = nn.MSELoss()

# ---------------------------------------------
# TRAINING
# ---------------------------------------------
epochs = 1500
for epoch in range(epochs):
    optimizer.zero_grad()
    y_pred = model(X_tensor)
    loss = loss_fn(y_pred, y_tensor)
    loss.backward()
    optimizer.step()
    
    if (epoch + 1) % 50 == 0:
        print(f"Epoch {epoch+1}, Loss = {loss.item():.4f}")

# ---------------------------------------------
# SAVE MODEL
# ---------------------------------------------
torch.save(model.state_dict(), "model/RD_model.pth")
print("\n✔ Model saved as RD_model.pth")
