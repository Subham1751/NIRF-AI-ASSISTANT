import joblib
import numpy as np

MODEL_PATH = "model/fppp_model.pkl"
model = joblib.load(MODEL_PATH)

print("Model loaded successfully.")

spon_2023 = float(input("Enter the Sponsored projects Amt(23-24): "))
spon_2022 = float(input("Enter the sponsored projects Amt(22-23): "))
spon_2021 = float(input("Enter the sponsored projects Amt(21-22): "))

consul_2023 = float(input("Enter the Consultancy projects Amt(23-24): "))
consul_2022 = float(input("Enter the Consultancy projects Amt(22-23): "))
consul_2021 = float(input("Enter the Consultancy projects Amt(21-22): "))

total_faculty = int(input("Enter total faculties: "))

avg_rf = (spon_2023 + spon_2022 + spon_2021) / 3
avg_cf = (consul_2023 + consul_2022 + consul_2021) / 3

rf_per_faculty = avg_rf / total_faculty
cf_per_faculty = avg_cf / total_faculty

print("\nEngineered Features:")
print(f"RF_per_faculty = {rf_per_faculty:.2f}")
print(f"CF_per_faculty = {cf_per_faculty:.2f}")

X = np.array([[rf_per_faculty, cf_per_faculty]])
predicted_fppp = model.predict(X)[0]

predicted_fppp = max(0, min(10, predicted_fppp))

print("\nPredicted FPPP Score:")
print(f"{predicted_fppp:.2f} / 10")
