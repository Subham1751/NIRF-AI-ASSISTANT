import pandas as pd

def load_medians():
    df = pd.read_excel("data/MasterData_SS.xlsx")
    return {
        "median_NT": df["TOTAL_SANCTIONED (Incl UG + PG)"].median(),
        "median_NE": df["TOTAL_ENROLLED"].median(),
        "median_NP": df["TOTAL_PHD_PURSUING"].median(),
        "median_SS": df["SS_Score"].median()
    }

def load_fsr_medians():
    df = pd.read_excel("data/MasterData_FSR.xlsx")

    return {
        "median_F": df["Full_Time_Reg_Faculty"].median(),
        "median_N": (df["Total_Sanctioned"] + df["Total_PhD_Enrolled_Students"]).median(),
        "median_FSR": df["FSR_Score"].median()
    }

def load_fru_medians():
    df = pd.read_csv("data/FRU_feature_engineered.csv")
    return {
        # Core FRU medians
        "median_BC": df["BC"].median(),
        "median_BO": df["BO"].median(),
        "median_FRU": df["FRU_Score"].median(),
        
        # Capital expenditure share medians
        "median_library_share": df["Library_pct_share"].median(),
        "median_lab_share": df["Lab_New_Equipment_Software_pct_share"].median(),
        "median_workshop_share": df["Engineering_Workshops_pct_share"].median(),
        "median_other_capex_share": df["Other_Expenditure_pct_share"].median(),

        # Operational expenditure share medians
        "median_salary_share": df["Salaries_pct_share"].median(),
        "median_infra_share": df["Academic_Infra_Maintenance_pct_share"].median(),
        "median_seminar_share": df["Seminars_Conferences_Workshops_pct_share"].median(),
    }