import pandas as pd

def load_raw_fru_data(path: str) -> pd.DataFrame:
    return pd.read_excel(path)

def compute_capital_features(df: pd.DataFrame) -> pd.DataFrame:
    df["CE1_per_student"] = df["Total_Capital_Expenditure_2023-24"] / df["Total_Admitted_Students_2023-2024"]
    df["CE2_per_student"] = df["Total_Capital_Expenditure_2022-2023"] / df["Total_Admitted_Students_2022-2023"]
    df["CE3_per_student"] = df["Total_Capital_Expenditure_2021-2022"] / df["Total_Admitted_Students_2021-2022"]
    
    df["BC"] = (df["CE1_per_student"] + df["CE2_per_student"] + df["CE3_per_student"]) / 3
    
    capital_heads = [
        "Library",
        "Lab_New_Equipment_Software",
        "Engineering_Workshops",
        "Other_Expenditure"
    ]
    
    for head in capital_heads:
        # Compute 3-year averages for capital expenditure heads per student
        c1 = df[f"{head}_2023-2024"] / df["Total_Admitted_Students_2023-2024"]
        c2 = df[f"{head}_2022-2023"] / df["Total_Admitted_Students_2022-2023"]
        c3 = df[f"{head}_2021-2022"] / df["Total_Admitted_Students_2021-2022"]
        avg_col = f"{head}_3yr_avg_per_student"
        df[avg_col] = (c1 + c2 + c3) / 3
        
        # Percentage share relative to total capital expenditure per student
        pct_col = f"{head}_pct_share"
        df[pct_col] = df[avg_col] / df["BC"]
    
    return df

def compute_operational_features(df: pd.DataFrame) -> pd.DataFrame:
    df["OE1_per_student"] = df["Total_Operational_Expenditure_2023-2024"] / df["Total_Admitted_Students_2023-2024"]
    df["OE2_per_student"] = df["Total_Operational_Expenditure_2022-2023"] / df["Total_Admitted_Students_2022-2023"]
    df["OE3_per_student"] = df["Total_Operational_Expenditure_2021-2022"] / df["Total_Admitted_Students_2021-2022"]
    
    df["BO"] = (df["OE1_per_student"] + df["OE2_per_student"] + df["OE3_per_student"]) / 3
    
    operational_heads = [
        "Salaries",
        "Academic_Infra_Maintenance",
        "Seminars_Conferences_Workshops"
    ]
    
    for head in operational_heads:
        # Compute 3-year averages for operational expenditure heads per student
        o1 = df[f"{head}_2023-2024"] / df["Total_Admitted_Students_2023-2024"]
        o2 = df[f"{head}_2022-2023"] / df["Total_Admitted_Students_2022-2023"]
        o3 = df[f"{head}_2021-2022"] / df["Total_Admitted_Students_2021-2022"]
        avg_col = f"{head}_3yr_avg_per_student"
        df[avg_col] = (o1 + o2 + o3) / 3
        
        # Percentage share relative to total operational expenditure per student
        pct_col = f"{head}_pct_share"
        df[pct_col] = df[avg_col] / df["BO"]
    
    return df

def compute_target(df: pd.DataFrame) -> pd.DataFrame:
    df["FRU_Score"] = pd.to_numeric(df["FRU_Score"], errors="coerce")
    return df

def enginner_fru_features(input_path: str, output_path: str):
    df = load_raw_fru_data(input_path)
    
    df = compute_capital_features(df)
    df = compute_operational_features(df)
    df = compute_target(df)
    
    fru_df = df[
        [
            # Core model features
            "BC",
            "BO",
            "FRU_Score",
            
            # Capital Expenditure (per student, 3-year avg)
            "Library_3yr_avg_per_student",
            "Lab_New_Equipment_Software_3yr_avg_per_student",
            "Engineering_Workshops_3yr_avg_per_student",
            "Other_Expenditure_3yr_avg_per_student",
            
            # Capital expenditure shares
            "Library_pct_share",
            "Lab_New_Equipment_Software_pct_share",
            "Engineering_Workshops_pct_share",
            "Other_Expenditure_pct_share",
            
            # Operational expenditure (per student, 3-year avg)
            "Salaries_3yr_avg_per_student",
            "Academic_Infra_Maintenance_3yr_avg_per_student",
            "Seminars_Conferences_Workshops_3yr_avg_per_student",
            
            # Operational expenditure shares
            "Salaries_pct_share",
            "Academic_Infra_Maintenance_pct_share",
            "Seminars_Conferences_Workshops_pct_share",
        ]
    ]
    
    # Save output
    fru_df.to_csv(output_path, index=False)
    print(f"[SUCCESS] FRU feature-engineered data saved to: {output_path}")
    
    
if __name__ == "__main__":
    enginner_fru_features(
        input_path = "data/MasterData_FRU.xlsx",
        output_path  ="data/FRU_feature_engineered.csv"
    )