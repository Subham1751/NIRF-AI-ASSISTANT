import joblib
import pandas as pd


def load_model(model_path="model/fru_model.pkl"):
    try:
        model = joblib.load(model_path)
        print("Model loaded successfully.")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None


def _validate_positive(*values, names=None):
    if names is None:
        names = [f"v{i}" for i in range(len(values))]
    for name, v in zip(names, values):
        if v is None:
            raise ValueError(f"{name} cannot be None.")
        if v < 0:
            raise ValueError(f"{name} cannot be negative.")
        if v == 0 and "students" in name.lower():
            raise ValueError(f"{name} cannot be zero (division by zero).")


def compute_bc_bo(
    students_y1: float,
    students_y2: float,
    students_y3: float,
    ce1_total: float,
    ce2_total: float,
    ce3_total: float,
    oe1_total: float,
    oe2_total: float,
    oe3_total: float,
):
    _validate_positive(
        students_y1, students_y2, students_y3,
        ce1_total, ce2_total, ce3_total,
        oe1_total, oe2_total, oe3_total,
        names=[
            "students_y1", "students_y2", "students_y3",
            "ce1_total", "ce2_total", "ce3_total",
            "oe1_total", "oe2_total", "oe3_total",
        ],
    )

    ce1_per_student = ce1_total / students_y1
    ce2_per_student = ce2_total / students_y2
    ce3_per_student = ce3_total / students_y3

    oe1_per_student = oe1_total / students_y1
    oe2_per_student = oe2_total / students_y2
    oe3_per_student = oe3_total / students_y3

    bc = (ce1_per_student + ce2_per_student + ce3_per_student) / 3
    bo = (oe1_per_student + oe2_per_student + oe3_per_student) / 3

    return bc, bo

def predict_fru(
    model,
    students_y1: float,
    students_y2: float,
    students_y3: float,
    ce1_total: float,
    ce2_total: float,
    ce3_total: float,
    oe1_total: float,
    oe2_total: float,
    oe3_total: float,
):
    bc, bo = compute_bc_bo(
        students_y1, students_y2, students_y3,
        ce1_total, ce2_total, ce3_total,
        oe1_total, oe2_total, oe3_total,
    )

    input_df = pd.DataFrame({
        "BC": [bc],
        "BO": [bo],
    })

    prediction = model.predict(input_df)[0]

    prediction = max(0.0, min(30.0, float(prediction)))

    return round(prediction, 3), round(bc, 3), round(bo, 3)


if __name__ == "__main__":
    print("\n--- FRU Score Prediction Tool ---\n")

    model = load_model()
    if model is None:
        exit()

    s1 = float(input("Enter Total Admitted Students (Year 1 / 2023-24): "))
    s2 = float(input("Enter Total Admitted Students (Year 2 / 2022-23): "))
    s3 = float(input("Enter Total Admitted Students (Year 3 / 2021-22): "))

    ce1 = float(input("Enter Capital Expenditure Total (Year 1 / 2023-24): "))
    ce2 = float(input("Enter Capital Expenditure Total (Year 2 / 2022-23): "))
    ce3 = float(input("Enter Capital Expenditure Total (Year 3 / 2021-22): "))

    oe1 = float(input("Enter Operational Expenditure Total (Year 1 / 2023-24): "))
    oe2 = float(input("Enter Operational Expenditure Total (Year 2 / 2022-23): "))
    oe3 = float(input("Enter Operational Expenditure Total (Year 3 / 2021-22): "))

    fru_score, bc, bo = predict_fru(model, s1, s2, s3, ce1, ce2, ce3, oe1, oe2, oe3)

    print(f"\nComputed BC (Avg CapEx per student, 3yr): {bc}")
    print(f"Computed BO (Avg OpEx per student, 3yr):  {bo}")
    print(f"\nPredicted FRU Score: {fru_score} / 30\n")